from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import os
# from app.config import (
#     DB_USER,
#     DB_PASSWORD,
#     DB_HOST,
#     DB_PORT,
#     DB_NAME,
# )

# DATABASE_URL = (
#     f"postgresql+psycopg://"
#     f"{DB_USER}:{DB_PASSWORD}"
#     f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )


DATABASE_URL = os.getenv("DATABASE_URL","postgresql+psycopg://admin:biRYani@localhost:5432/test")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


