from fastapi import FastAPI
from my_api.app.api.api_v1 import api
from my_api.app.models.base import BaseClass
from my_api.app.database.session import engine
import uvicorn


app = FastAPI()
app.include_router(api.router)

if __name__ =="__main__":
    #BaseClass.metadata.create_all(bind=engine)
    uvicorn.run(app, port=8000)