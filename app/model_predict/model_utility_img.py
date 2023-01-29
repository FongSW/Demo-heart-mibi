import pandas as pd
import numpy as np
import shutil, pickle
import tensorflow as tf
from tensorflow.keras.models import load_model
import pickle, os
import lightgbm as lgb
from glob2 import glob
import ast
import xgboost as xgb

from datetime import datetime


def load_best_model():

    log_model_folder = glob('app/model_predict/classification_model/*model*')[0]
    file_d = open(log_model_folder, "rb")
    # current_model = lgb.Booster(model_file=log_model_folder)
    current_model = pickle.load(file_d)
    return current_model

def predict_labal(model, x, type_model):
    threshold = 0.5
    if type_model == 'XGBoost':
        data = xgb.DMatrix(x)

        if model.predict(data) >= threshold:
            pred = 1
        else:
            pred = 0  
    elif type_model == 'LightGBM':
        if model.predict(x) >= threshold:
            pred = 1
        else:
            pred = 0    
    elif type_model == 'SGD':
        pred = model.predict(x)
    return pred

def info_model():
  # find parameter
  log_param_folder = glob('app/model_predict/info_model/*.txt')[0]

  f = open(log_param_folder, 'r')
  if f.mode=='r':
    contents= f.read()
  # using ast.literal_eval()
  # convert dictionary string to dictionary
  dict_param = ast.literal_eval(contents)
  return dict_param

def load_accuracy_date_create_model():
    model_df = pd.read_csv("/data_log/log_train_model/log_train_quantitative_model.csv")
    best_model_info = model_df[model_df['description'] == "Best model"].iloc[-1] 

    return best_model_info.test_accuracy, datetime.strptime(best_model_info.timestamp, '%Y-%m-%d %H:%M:%S.%f').strftime('%d/%m/%y'), best_model_info.type_of_model

