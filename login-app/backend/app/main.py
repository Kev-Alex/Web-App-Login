from typing import Literal
import asyncpg # type: ignore
from fastapi import FastAPI, Depends, HTTPException # type: ignore
from pydantic import BaseModel, EmailStr # type: ignore

from config import settings
from app import db

app = FastAPI(
    title="WebLogin API",
    version="0.1.0",
    description="API mínima para login (FastAPI + PostgreSQL)",
)

@app.on_event("startup")
async def _startup() -> None:
    await db.startup()

@app.on_event("shutdown")
async def _shutdown() -> None:
    await db.shutdown()

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    message: Literal["ok"]

@app.get("/api/health/db", tags=["system"])
async def health_db(conn: asyncpg.Connection = Depends(db.get_conn)):
    try:
        row = await conn.fetchval("SELECT 1;")
        return {"db": "ok", "result": row}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"db_error: {e!s}")

_SQL_LOGIN = '''
    SELECT id
    FROM public.users
    WHERE email = $1
      AND password = crypt($2, password)
    LIMIT 1;
'''

@app.post("/api/login", response_model=LoginResponse, tags=["auth"])
async def login(payload: LoginRequest, conn: asyncpg.Connection = Depends(db.get_conn)):
    user_id = await conn.fetchval(_SQL_LOGIN, payload.email, payload.password)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return LoginResponse(message="ok")
