from fastapi import FastAPI
from router import routes

app = FastAPI()

app.include_router(router=routes.router)

@app.get('/')
def landingpage():
    return {"landing page"}