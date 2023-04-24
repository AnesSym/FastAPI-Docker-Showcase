from typing import List
from my_api.app.models.tables import Jobs
from my_api.app.database.session import db
from my_api.app.schemas.jobs import JobSchema
from fastapi import APIRouter

jobs_router = APIRouter()

@jobs_router.get("/jobs", response_model=List[JobSchema])
def read_jobs():
    jobs = db.query(Jobs).all() 
    return jobs