from sqlalchemy import ForeignKey, Column, String, Integer, Date
from my_api.app.models.base import BaseClass
from sqlalchemy.orm import relationship





class Company(BaseClass):

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    jobs = relationship("Jobs", back_populates="company")
    

class Jobs(BaseClass):
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    location_id = Column(Integer, ForeignKey("location.id"))
    company_id = Column(Integer, ForeignKey("company.id"))
    company = relationship("Company", back_populates="jobs")
    location = relationship("Location", back_populates="jobs")



class Location(BaseClass):
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    jobs = relationship("Jobs", back_populates="location")

    


