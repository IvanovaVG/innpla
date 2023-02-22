import uvicorn
from fastapi import APIRouter, FastAPI

from api.handlers import user_router
#from config.celery_config import create_celery


app = FastAPI(title='INNPLA', version="0.0.1", openapi_url="/api/v1/openapi.json")

#app.celery_app = create_celery()

main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix='/user', tags=['user'])
app.include_router(main_api_router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
