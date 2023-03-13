from fastapi import FastAPI

from routers import router

app = FastAPI()

@app.get('/')
def get_root():
    return {"message": "api de papeis"}

app.include_router(router, prefix='')