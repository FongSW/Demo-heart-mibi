from fastapi import APIRouter, File, UploadFile, Form, Depends, Body
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import shutil, pickle
import glob
import subprocess

#import the connection to postgres
from app.config.connection_db import con_db

#import ORM DB 
from app.model.patient_db import patient_features as patient_features_table

#import db schema
from app.schema.patient_schema import patient_schema, inference_ocr_schema
from app.schema.utility_schema import UserSchema, UserLoginSchema

#import JWT
from app.auth.jwt_bearer import JWTBearer
from app.auth.jwt_handler import signJWT

# import model prediction
from app.model_predict.model_utility_img import load_best_model, predict_labal, load_accuracy_date_create_model, info_model
from app.model_predict.pre_process import pre_processing

inference_route = APIRouter(prefix='/inference', tags=['inference'], responses={404: {"description": "Not found"}})

@inference_route.post("/ocr/per-patient-per-vessel/")
async def inference_per_patient_per_vessel(data: inference_ocr_schema):
    # sum feature data
    numerical_feature = data.values
    for n in list(data.patient_characteristic.values()):
        numerical_feature.append(n)
    # get and prepare data 
    X_features = pre_processing(numerical_feature)
    # load model
    current_model = load_best_model()
    # cheak type model
    info_current_model = info_model()
    # predict class
    result_predict_cag = predict_labal(current_model, X_features, info_current_model["type_of_model"])
    print("result CAG : ", result_predict_cag)

    result_predict_cag = int(result_predict_cag)
    #Demo
    result_predict_vessel_1 = 1
    result_predict_vessel_2 = 1
    result_predict_vessel_3 = 1
    return {
        "vessel_1" : result_predict_vessel_1,
        "vessel_2" : result_predict_vessel_2,
        "vessel_3" : result_predict_vessel_3,
        "predict_cag" : result_predict_cag
    }

@inference_route.post("/ocr/vessel/")
async def inference_vessel(data: inference_ocr_schema):
    result_predict_vessel_1 = 1
    result_predict_vessel_2 = 1
    result_predict_vessel_3 = 1
    return {
        "vessel_1" : result_predict_vessel_1,
        "vessel_2" : result_predict_vessel_2,
        "vessel_3" : result_predict_vessel_3,
    }


@inference_route.post("/ocr/patient/")
async def inference_patient(data: inference_ocr_schema):
    # sum feature data
    numerical_feature = data.values
    for n in list(data.patient_characteristic.values()):
        numerical_feature.append(n)
    # get and prepare data 
    X_features = pre_processing(numerical_feature)
    # load model
    current_model = load_best_model()
    # cheak type model
    info_current_model = info_model()
    # predict class
    result_predict_cag = predict_labal(current_model, X_features, info_current_model["type_of_model"])
    print("result CAG : ", result_predict_cag)

    result_predict_cag = int(result_predict_cag)
    return {
        "predict_cag" : result_predict_cag
    }
