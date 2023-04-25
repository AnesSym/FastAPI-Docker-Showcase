
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from my_api.app.core.config import settings
#from app.core.config import settings

engine = create_engine("sqlite:///my_api/mydb.db", pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

