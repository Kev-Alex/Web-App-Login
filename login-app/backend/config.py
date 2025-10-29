from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    app_host: str = Field(default="0.0.0.0")
    app_port: int = Field(default=8081)

    db_host: str = Field(default="db")
    db_port: int = Field(default=5432)
    db_name: str = Field(default="login_db")
    db_user: str = Field(default="webuser")
    db_password: str = Field(default="webpass")

    database_url: str | None = None  # si la defines, tiene prioridad

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    def dsn(self) -> str:
        if self.database_url:
            return self.database_url
        return (
            f"postgresql://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

settings = Settings()
