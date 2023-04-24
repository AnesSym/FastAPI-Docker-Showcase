from sqlalchemy import ForeignKey, Column, String, Integer, Date
from my_api.app.models.base import BaseClass



class Jobs(BaseClass):
    
    job_id = Column("job_id", Integer, primary_key=True)
    job_title = Column("job_title", String)
    job_description = Column("job_description", String)
    job_requirements = Column("job_requirementes", String)
    job_salary = Column("job_salary", Integer)
    company_id = Column("company_id", Integer, ForeignKey("company.company_id"))
    

class Company(BaseClass):
    __tablename__ = "company"
    company_id = Column("company_id", Integer, primary_key=True)
    company_name = Column("company_name", String)
    company_description = Column("company_description", String)
    company_website = Column("company_website", String)
    company_size = Column("company_size", Integer)
    company_founded_date = Column("company_founded_date", Date)
    locaton_id = Column("location_id", Integer, ForeignKey("location.location_id"))
    

class Location(BaseClass):
    __tablename__ = "location"
    location_id = Column("location_id", Integer, primary_key=True)
    location_adress = Column("location_adress", String)
    location_city = Column("location_city", String)
    location_state = Column("location_state", String)
    location_country = Column("location_country", String)
    


