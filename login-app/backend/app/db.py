import asyncpg
from config import settings

_pool: asyncpg.Pool | None = None

async def startup() -> None:
    """Inicializa el pool de conexiones."""
    global _pool
    if _pool is None:
        _pool = await asyncpg.create_pool(dsn=settings.dsn(), min_size=1, max_size=5)
        print(f"✅ Database pool initialized -> {settings.dsn()}")

async def shutdown() -> None:
    """Cierra el pool de conexiones al apagar la app."""
    global _pool
    if _pool is not None:
        await _pool.close()
        _pool = None
        print("🛑 Database pool closed.")

async def get_conn():
    """Provee una conexión temporal desde el pool."""
    if _pool is None:
        raise RuntimeError("DB pool not initialized")
    conn = await _pool.acquire()
    try:
        yield conn
    finally:
        await _pool.release(conn)
