from fastapi import APIRouter
from my_api.app.api.api_v1.endpoints.jobs import jobs_router
from my_api.app.api.api_v1.endpoints.company import company_router
from my_api.app.api.api_v1.endpoints.location import location_router

router = APIRouter()

router.include_router(jobs_router)
router.include_router(location_router)
router.include_router(company_router)