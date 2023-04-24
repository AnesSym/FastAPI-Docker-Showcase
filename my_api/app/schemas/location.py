from pydantic import BaseModel

class LocationSchema(BaseModel):
    id: int
    name: str