import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient

from misc.env import DBSettings
from routes.routes import router

app = FastAPI()
app.include_router(router)


@app.on_event('startup')
def startup():
    app.mongodb_client = MongoClient(DBSettings.HOST)
    app.database = app.mongodb_client.notifications_db


@app.on_event('shutdown')
def shutdown():
    app.mongodb_client.close()


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
