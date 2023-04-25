from typing import List
from my_api.app.models.tables import Company
from my_api.app.database.session import db
from my_api.app.schemas.company import CompanySchema
from fastapi import APIRouter

company_router = APIRouter()

@company_router.get("/company", response_model=List[CompanySchema])
def read_companies():
    companies = db.query(Company).all()
    return companies