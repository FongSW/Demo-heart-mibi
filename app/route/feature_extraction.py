from fastapi import APIRouter, File, UploadFile, Form, Depends, Body
from datetime import datetime, timedelta
import shutil, pickle
import glob
import subprocess

import pickle, os
import ast

import zipfile

from starlette.responses import JSONResponse


from app.celery.celery_task import ocr_extract_task
from app.celery.celery_utils import get_task_info
from celery import group

from app.schema.utility_schema import ocr_schema

extraction_route = APIRouter(prefix='/feature_extraction', tags=['feature_extraction'], responses={404: {"description": "Not found"}})

@extraction_route.get("/{task_id}")
async def get_task_status(task_id: str) -> dict:
    """
    Return the status of the submitted Task
    """
    return get_task_info(task_id)

@extraction_route.post("/")
async def extract_image(data: ocr_schema):
    # Extract data
    task = ocr_extract_task.apply_async(args=[data.hn, data.client_root_path], countdown=10)     
    return JSONResponse({"task_id": task.id})