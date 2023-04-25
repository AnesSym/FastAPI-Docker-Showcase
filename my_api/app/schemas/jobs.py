from pydantic import BaseModel
from typing import List
from my_api.app.schemas import location, company


class JobSchema(BaseModel):
    id: int
    title: str
    description: str
    location: location.LocationSchema
    company: company.CompanySchema

class JobsListSchema(BaseModel):
    jobs: List[JobSchema]