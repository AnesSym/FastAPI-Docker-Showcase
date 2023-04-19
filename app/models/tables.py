from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, DateTime, Date
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Jobs(Base):
    __tablename__ = "jobs"
    job_id = Column("job_id", Integer, primary_key=True)
    job_title = Column("job_title", String)
    job_description = Column("job_description", String)
    job_requirements = Column("job_requirementes", String)
    job_salary = Column("job_salary", Integer)
    job_post_date = Column(DateTime(timezone=True), server_default = func.now())
    company_id = Column("company_id", Integer, ForeignKey("company.company_id"))
    


class Company(Base):
    __tablename__ = "company"
    company_id = Column("company_id", Integer, primary_key=True)
    company_name = Column("company_name", String)
    company_description = Column("company_description", String)
    company_website = Column("company_website", String)
    company_size = Column("company_size", Integer)
    company_founded_date = Column("company_founded_date", Date)
    locaton_id = Column("location_id", Integer, ForeignKey("location.location_id"))
    
    

class Location(Base):
    __tablename__ = "location"
    location_id = Column("location_id", Integer, primary_key=True)
    location_adress = Column("location_adress", String)
    location_city = Column("location_city", String)
    location_state = Column("location_state", String)
    location_country = Column("location_country", String)
    


#the next lines of code are temporarily here and only for practise and testing.
engine = create_engine("sqlite:///mydb.db", echo = True)

Base.metadata.create_all(bind = engine)

Session = sessionmaker(bind = engine)

session = Session()

