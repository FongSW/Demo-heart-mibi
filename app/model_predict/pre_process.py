#other utility packages
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

from sklearn import preprocessing
from sklearn.preprocessing import FunctionTransformer
from sklearn.decomposition import PCA

def init_feature(df_X):
    #mpi feature
    initFeature = df_X[[c for c in df_X if c not in ['gender']]]
    return initFeature

from sklearn.preprocessing import OneHotEncoder

def getOnehotencoderSex(df_X):
  if(df_X.values == "M"):
    sex_list = ["1", "0"]
  else:
    sex_list = ["0", "1"]
  sexDummy = pd.DataFrame(data=[sex_list], columns=["F", "M"])
  return sexDummy

def extractFeat(df_X):
    
    featX = df_X.copy()
    init_feat = init_feature(featX)
    sex_feat = getOnehotencoderSex(featX['gender'])

        
    #concat features
    featX.reset_index(drop=True, inplace=True)
    final_featX = pd.concat([init_feat, sex_feat], axis=1)
    final_featX['F'] = final_featX['F'].astype(int)
    final_featX['M'] = final_featX['M'].astype(int)
    final_featX = final_featX.loc[:, ~final_featX.columns.str.match('Unnamed')]
    # feat = feat.drop("Gender", axis=1)
    
    return final_featX

def standard_scale(df, column):
  if(type(column) != str):
    X = df.values
    scaler = preprocessing.Normalizer()
    scaler.fit(X)
    X_scaled = scaler.transform(X)
    df = pd.DataFrame(data = X_scaled, columns=column)
  return df

def min_max_scale(df, column):
  if(type(column) != str):
    X = df.values
    scaler = preprocessing.Normalizer()
    scaler.fit(X)
    X_scaled = scaler.transform(X)
    df = pd.DataFrame(data = X_scaled, columns=column)
  return df

def normalize(df, column):
  if(type(column) != str):
    X = df.values
    scaler = preprocessing.Normalizer()
    scaler.fit(X)
    X_scaled = scaler.transform(X)
    df = pd.DataFrame(data = X_scaled, columns=column)
  return df

def log_transform(df, column):
    print(df)
    X = abs(df.values)
    scaler = FunctionTransformer(np.log)
    scaler.fit(X)
    X_scaled = scaler.transform(X +1)
    column = [str(col) + '_log' for col in column]
    df = pd.DataFrame(data = X_scaled, columns=column)
    return df

def standard_scale(df, column):
  if(type(column) != str):
    X = df.values
    scaler = preprocessing.Normalizer()
    scaler.fit(X)
    X_scaled = scaler.transform(X)
    df = pd.DataFrame(data = X_scaled, columns=column)
  return df

def min_max_scale(df, column):
  if(type(column) != str):
    X = df.values
    scaler = preprocessing.Normalizer()
    scaler.fit(X)
    X_scaled = scaler.transform(X)
    df = pd.DataFrame(data = X_scaled, columns=column)
  return df

def normalize(df, column):
  if(type(column) != str):
    X = df.values
    scaler = preprocessing.Normalizer()
    scaler.fit(X)
    X_scaled = scaler.transform(X)
    df = pd.DataFrame(data = X_scaled, columns=column)
  return df

def log_transform(df, column):
    print(df)
    X = abs(df.values)
    scaler = FunctionTransformer(np.log)
    scaler.fit(X)
    X_scaled = scaler.transform(X +1)
    column = [str(col) + '_log' for col in column]
    df = pd.DataFrame(data = X_scaled, columns=column)
    return df

from sklearn.manifold import TSNE
from sklearn.decomposition import TruncatedSVD

def decomposition(df, target, algorithm):
  algorithm = algorithm.upper()
  target = target.upper()
  if(algorithm == "PCA"):
    decompose_algo = PCA(n_components=1)
  elif(algorithm == "TNSE"):
    decompose_algo = TSNE(n_components=1)
  elif(algorithm == "LSA"):
    decompose_algo = TruncatedSVD(n_components=1)
  if(target == "PC"):
    split_df = df[[c for c in df if c in ['F', 'M', 'Age', 'BMI', 'DM', 'HT', 'DLP', 'CKD']]]
    components = decompose_algo.fit_transform(split_df.values)
    decompose_df = pd.DataFrame(data = components, columns = [target+'_'+algorithm+'_features'])
  elif(target == "LAD" or target == "LCX" or target == "RCA" or target == "TOT"):
    split_df = [col for col in df.columns if target in col]
    split_df_tnse_columns = df[[c for c in df.columns if c in split_df]]
    components = decompose_algo.fit_transform(split_df_tnse_columns.values)
    decompose_df = pd.DataFrame(data = components, columns = [target+'_'+algorithm+'_features'])
  return decompose_df
  
def pre_processing(numerical_feature):

    # get data
    # data = [numerical_feature.S_MaxPerfusion, numerical_feature.S_Intervals, numerical_feature.S_ED, numerical_feature.S_ES, numerical_feature.S_EF, numerical_feature.SM_LADPerfusion, numerical_feature.SSD_LADPerfusion, numerical_feature.SM_LCXPerfusion, numerical_feature.SSD_LCXPerfusion, numerical_feature.SM_RCAPerfusion, numerical_feature.SSD_RCAPerfusion, numerical_feature.SM_TOTPerfusion, numerical_feature.SSD_TOTPerfusion, numerical_feature.SM_LADWallThickening, numerical_feature.SSD_LADWallThickening, numerical_feature.SM_LCXWallThickening, numerical_feature.SSD_LCXWallThickening, numerical_feature.SM_RCAWallThickening, numerical_feature.SSD_RCAWallThickening, numerical_feature.SM_TOTWallThickening, numerical_feature.SSD_TOTWallThickening, numerical_feature.SM_LADWallMotion, numerical_feature.SSD_LADWallMotion, numerical_feature.SM_LCXWallMotion, numerical_feature.SSD_LCXWallMotion, numerical_feature.SM_RCAWallMotion, numerical_feature.SSD_RCAWallMotion, numerical_feature.SM_TOTWallMotion, numerical_feature.SSD_TOTWallMotion, numerical_feature.SE_LADPerfusion, numerical_feature.SE_LCXPerfusion, numerical_feature.SE_RCAPerfusion, numerical_feature.SE_TOTPerfusion, numerical_feature.SE_LADWallThickening, numerical_feature.SE_LCXWallThickening, numerical_feature.SE_RCAWallThickening, numerical_feature.SE_TOTWallThickening, numerical_feature.SE_LADWallMotion, numerical_feature.SE_LCXWallMotion, numerical_feature.SE_RCAWallMotion, numerical_feature.SE_TOTWallMotion, numerical_feature.SSEV_LADPerfusion, numerical_feature.SSEV_LCXPerfusion, numerical_feature.SSEV_RCAPerfusion, numerical_feature.SSEV_TOTPerfusion, numerical_feature.SSEV_LADWallThickening, numerical_feature.SSEV_LCXWallThickening, numerical_feature.SSEV_RCAWallThickening, numerical_feature.SSEV_TOTWallThickening, numerical_feature.SSEV_LADWallMotion, numerical_feature.SSEV_LCXWallMotion, numerical_feature.SSEV_RCAWallMotion, numerical_feature.SSEV_TOTWallMotion, numerical_feature.R_MaxPerfusion, numerical_feature.R_Intervals, numerical_feature.R_ED, numerical_feature.R_ES, numerical_feature.R_EF, numerical_feature.RM_LADPerfusion, numerical_feature.RSD_LADPerfusion, numerical_feature.RM_LCXPerfusion, numerical_feature.RSD_LCXPerfusion, numerical_feature.RM_RCAPerfusion, numerical_feature.RSD_RCAPerfusion, numerical_feature.RM_TOTPerfusion, numerical_feature.RSD_TOTPerfusion, numerical_feature.RM_LADWallThickening, numerical_feature.RSD_LADWallThickening, numerical_feature.RM_LCXWallThickening, numerical_feature.RSD_LCXWallThickening, numerical_feature.RM_RCAWallThickening, numerical_feature.RSD_RCAWallThickening, numerical_feature.RM_TOTWallThickening, numerical_feature.RSD_TOTWallThickening, numerical_feature.RM_LADWallMotion, numerical_feature.RSD_LADWallMotion, numerical_feature.RM_LCXWallMotion, numerical_feature.RSD_LCXWallMotion, numerical_feature.RM_RCAWallMotion, numerical_feature.RSD_RCAWallMotion, numerical_feature.RM_TOTWallMotion, numerical_feature.RSD_TOTWallMotion, numerical_feature.RE_LADPerfusion, numerical_feature.RE_LCXPerfusion, numerical_feature.RE_RCAPerfusion, numerical_feature.RE_TOTPerfusion, numerical_feature.RE_LADWallThickening, numerical_feature.RE_LCXWallThickening, numerical_feature.RE_RCAWallThickening, numerical_feature.RE_TOTWallThickening, numerical_feature.RE_LADWallMotion, numerical_feature.RE_LCXWallMotion, numerical_feature.RE_RCAWallMotion, numerical_feature.RE_TOTWallMotion, numerical_feature.RSEV_LADPerfusion, numerical_feature.RSEV_LCXPerfusion, numerical_feature.RSEV_RCAPerfusion, numerical_feature.RSEV_TOTPerfusion, numerical_feature.RSEV_LADWallThickening, numerical_feature.RSEV_LCXWallThickening, numerical_feature.RSEV_RCAWallThickening, numerical_feature.RSEV_TOTWallThickening, numerical_feature.RSEV_LADWallMotion, numerical_feature.RSEV_LCXWallMotion, numerical_feature.RSEV_RCAWallMotion, numerical_feature.RSEV_TOTWallMotion, numerical_feature.SSS, numerical_feature.S_STS, numerical_feature.S_SMS, numerical_feature.SRS, numerical_feature.R_STS, numerical_feature.R_SMS, numerical_feature.age, numerical_feature.gender, numerical_feature.bmi, numerical_feature.dm, numerical_feature.ht, numerical_feature.dlp, numerical_feature.ckd]
    columns_name = ["S_MaxPerfusion", "S_Intervals", "S_ED", "S_ES", "S_EF", "SM_LADPerfusion", "SSD_LADPerfusion", "SM_LCXPerfusion", "SSD_LCXPerfusion", "SM_RCAPerfusion", "SSD_RCAPerfusion", "SM_TOTPerfusion", "SSD_TOTPerfusion", "SM_LADWallThickening", "SSD_LADWallThickening", "SM_LCXWallThickening", "SSD_LCXWallThickening", "SM_RCAWallThickening", "SSD_RCAWallThickening", "SM_TOTWallThickening", "SSD_TOTWallThickening", "SM_LADWallMotion", "SSD_LADWallMotion", "SM_LCXWallMotion", "SSD_LCXWallMotion", "SM_RCAWallMotion", "SSD_RCAWallMotion", "SM_TOTWallMotion", "SSD_TOTWallMotion", "SE_LADPerfusion", "SE_LCXPerfusion", "SE_RCAPerfusion", "SE_TOTPerfusion", "SE_LADWallThickening", "SE_LCXWallThickening", "SE_RCAWallThickening", "SE_TOTWallThickening", "SE_LADWallMotion", "SE_LCXWallMotion", "SE_RCAWallMotion", "SE_TOTWallMotion", "SSEV_LADPerfusion", "SSEV_LCXPerfusion", "SSEV_RCAPerfusion", "SSEV_TOTPerfusion", "SSEV_LADWallThickening", "SSEV_LCXWallThickening", "SSEV_RCAWallThickening", "SSEV_TOTWallThickening", "SSEV_LADWallMotion", "SSEV_LCXWallMotion", "SSEV_RCAWallMotion", "SSEV_TOTWallMotion", "R_MaxPerfusion", "R_Intervals", "R_ED", "R_ES", "R_EF", "RM_LADPerfusion", "RSD_LADPerfusion", "RM_LCXPerfusion", "RSD_LCXPerfusion", "RM_RCAPerfusion", "RSD_RCAPerfusion", "RM_TOTPerfusion", "RSD_TOTPerfusion", "RM_LADWallThickening", "RSD_LADWallThickening", "RM_LCXWallThickening", "RSD_LCXWallThickening", "RM_RCAWallThickening", "RSD_RCAWallThickening", "RM_TOTWallThickening", "RSD_TOTWallThickening", "RM_LADWallMotion", "RSD_LADWallMotion", "RM_LCXWallMotion", "RSD_LCXWallMotion", "RM_RCAWallMotion", "RSD_RCAWallMotion", "RM_TOTWallMotion", "RSD_TOTWallMotion", "RE_LADPerfusion", "RE_LCXPerfusion", "RE_RCAPerfusion", "RE_TOTPerfusion", "RE_LADWallThickening", "RE_LCXWallThickening", "RE_RCAWallThickening", "RE_TOTWallThickening", "RE_LADWallMotion", "RE_LCXWallMotion", "RE_RCAWallMotion", "RE_TOTWallMotion", "RSEV_LADPerfusion", "RSEV_LCXPerfusion", "RSEV_RCAPerfusion", "RSEV_TOTPerfusion", "RSEV_LADWallThickening", "RSEV_LCXWallThickening", "RSEV_RCAWallThickening", "RSEV_TOTWallThickening", "RSEV_LADWallMotion", "RSEV_LCXWallMotion", "RSEV_RCAWallMotion", "RSEV_TOTWallMotion", "SSS", "S_STS", 'S_SMS', 'SRS', 'R_STS', 'R_SMS', "Age", "Gender", "BMI", "DM", "HT", "DLP", "CKD"]
    arrange_col = ['age', 'gender', 'bmi', 'dm', 'ht', 'dlp', 'ckd', 'rm_ladperfusion', 'se_ladperfusion', 'se_ladwallmotion', 'se_ladwallthickening', 'se_lcxperfusion', 'se_lcxwallmotion', 'se_lcxwallthickening', 'se_rcaperfusion', 'se_rcawallmotion', 'se_rcawallthickening', 'se_totperfusion', 'se_totwallmotion', 'se_totwallthickening', 'sm_ladperfusion', 'sm_ladwallmotion', 'sm_ladwallthickening', 'sm_lcxperfusion', 'sm_lcxwallmotion', 'sm_lcxwallthickening', 'sm_rcaperfusion', 'sm_rcawallmotion', 'sm_rcawallthickening', 'sm_totperfusion', 'sm_totwallmotion', 'sm_totwallthickening', 'ssd_ladperfusion', 'ssd_ladwallmotion', 'ssd_ladwallthickening', 'ssd_lcxperfusion', 'ssd_lcxwallmotion', 'ssd_lcxwallthickening', 'ssd_rcaperfusion', 'ssd_rcawallmotion', 'ssd_rcawallthickening', 'ssd_totperfusion', 'ssd_totwallmotion', 'ssd_totwallthickening', 'ssev_ladperfusion', 'ssev_ladwallmotion', 'ssev_ladwallthickening', 'ssev_lcxperfusion', 'ssev_lcxwallmotion', 'ssev_lcxwallthickening', 'ssev_rcaperfusion', 'ssev_rcawallmotion', 'ssev_rcawallthickening', 'ssev_totperfusion', 'ssev_totwallmotion', 'ssev_totwallthickening', 's_ed', 's_ef', 's_es', 's_intervals', 's_maxperfusion', 're_ladperfusion', 're_ladwallmotion', 're_ladwallthickening', 're_lcxperfusion', 're_lcxwallmotion', 're_lcxwallthickening', 're_rcaperfusion', 're_rcawallmotion', 're_rcawallthickening', 're_totperfusion', 're_totwallmotion', 're_totwallthickening', 'rm_ladwallmotion', 'rm_ladwallthickening', 'rm_lcxperfusion', 'rm_lcxwallmotion', 'rm_lcxwallthickening', 'rm_rcaperfusion', 'rm_rcawallmotion', 'rm_rcawallthickening', 'rm_totperfusion', 'rm_totwallmotion', 'rm_totwallthickening', 'rsd_ladperfusion', 'rsd_ladwallmotion', 'rsd_ladwallthickening', 'rsd_lcxperfusion', 'rsd_lcxwallmotion', 'rsd_lcxwallthickening', 'rsd_rcaperfusion', 'rsd_rcawallmotion', 'rsd_rcawallthickening', 'rsd_totperfusion', 'rsd_totwallmotion', 'rsd_totwallthickening', 'rsev_ladperfusion', 'rsev_ladwallmotion', 'rsev_ladwallthickening', 'rsev_lcxperfusion', 'rsev_lcxwallmotion', 'rsev_lcxwallthickening', 'rsev_rcaperfusion', 'rsev_rcawallmotion', 'rsev_rcawallthickening', 'rsev_totperfusion', 'rsev_totwallmotion', 'rsev_totwallthickening', 'r_ed', 'r_ef', 'r_es', 'r_intervals', 'r_maxperfusion', 'r_sms', 'r_sts', 'srs', 'sss', 's_sms', 's_sts']
    feat_x = pd.DataFrame(data=[numerical_feature], columns=columns_name)
    print("df >>>",feat_x.shape)
    feat_x.columns = [x.lower() for x in feat_x.columns]
    feat_x = feat_x[arrange_col]
    #5. extract features
    feat = extractFeat(feat_x)

    # 6. normalize
    feat_scale = feat.copy()
    print(feat_scale.values)
    feat_scale_normalize = normalize(feat_scale, feat_scale.columns)
    feat_scale_log = log_transform(feat_scale, feat_scale.columns)
    feat_scale_concat = pd.concat([feat_scale_normalize, feat_scale_log], axis=1)
    
    print(feat_scale_concat.shape)
    print(feat_scale_concat)
    feat_corr = feat_scale_concat
    
    return feat_corr