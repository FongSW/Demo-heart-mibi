from fastapi import FastAPI, File, UploadFile
import uvicorn as uvicorn
#import router
from app.route.api_router import api_route
from app.route.test_route import test_route
from app.route.inference import inference_route
from app.route.feature_extraction import extraction_route
from app.celery.celery_utils import create_celery

def create_app() -> FastAPI:
    current_app = FastAPI(title="Web Heart-mibi")
    current_app.celery_app = create_celery()
    current_app.include_router(inference_route)
    current_app.include_router(extraction_route)
    return current_app

app = create_app()
celery = app.celery_app

# if __name__ == "__main__":
#     uvicorn.run("app.index:app",host="0.0.0.0", port=8001, reload=True)