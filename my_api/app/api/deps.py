from typing import Generator
from my_api.app.database.session import SessionLocal


def get_db() -> Generator:

    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()