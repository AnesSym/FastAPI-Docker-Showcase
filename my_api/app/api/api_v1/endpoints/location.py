from typing import List
from my_api.app.models.tables import Location
from my_api.app.database.session import db
from my_api.app.schemas.location import LocationSchema
from fastapi import APIRouter

location_router = APIRouter()

@location_router.get("/location", response_model=List[LocationSchema])
def read_locations():
    locations = db.query(Location).all()
    return locations