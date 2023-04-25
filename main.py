from fastapi import FastAPI
from my_api.app.models.base import BaseClass
from my_api.app.core.config import settings
from my_api.app.api.api_v1 import api
from my_api.app.database.session import engine
import uvicorn


app = FastAPI()
app.include_router(api.router)

if __name__ =="__main__":
    BaseClass.metadata.create_all(bind=engine)
    uvicorn.run(app, host="0.0.0.0", port=7000)