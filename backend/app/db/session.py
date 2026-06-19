from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[SessionLocal, None, None]:
    """Injeta a sessao do banco de dados nas rotas/servicos e fecha apos o uso"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
