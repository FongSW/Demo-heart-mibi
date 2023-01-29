from datetime import datetime
from pydantic import BaseModel
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, Field, EmailStr



class patient_schema(BaseModel):
#----------------------------------------------------------------------
    patient_id: int
    S_MaxPerfusion: int
    S_Intervals: int
    S_ED: int
    S_ES: int
    S_EF: int   
    SM_LADPerfusion: float
    SSD_LADPerfusion: float
    SM_LCXPerfusion: float
    SSD_LCXPerfusion: float
    SM_RCAPerfusion: float
    SSD_RCAPerfusion: float
    SM_TOTPerfusion: float
    SSD_TOTPerfusion: float
    SM_LADWallThickening: float
    SSD_LADWallThickening: float
    SM_LCXWallThickening: float
    SSD_LCXWallThickening: float
    SM_RCAWallThickening: float
    SSD_RCAWallThickening: float
    SM_TOTWallThickening: float
    SSD_TOTWallThickening: float
    SM_LADWallMotion: float
    SSD_LADWallMotion: float
    SM_LCXWallMotion: float
    SSD_LCXWallMotion: float
    SM_RCAWallMotion: float
    SSD_RCAWallMotion: float
    SM_TOTWallMotion: float
    SSD_TOTWallMotion: float       
    SE_LADPerfusion: int
    SE_LCXPerfusion: int
    SE_RCAPerfusion: int
    SE_TOTPerfusion: int
    SE_LADWallThickening: int
    SE_LCXWallThickening: int
    SE_RCAWallThickening: int
    SE_TOTWallThickening: int
    SE_LADWallMotion: int
    SE_LCXWallMotion: int
    SE_RCAWallMotion: int
    SE_TOTWallMotion: int
    SSEV_LADPerfusion: float
    SSEV_LCXPerfusion: float
    SSEV_RCAPerfusion: float
    SSEV_TOTPerfusion: float
    SSEV_LADWallThickening: float
    SSEV_LCXWallThickening: float
    SSEV_RCAWallThickening: float
    SSEV_TOTWallThickening: float
    SSEV_LADWallMotion: float
    SSEV_LCXWallMotion: float
    SSEV_RCAWallMotion: float
    SSEV_TOTWallMotion: float
    R_MaxPerfusion: int
    R_Intervals: int
    R_ED: int
    R_ES: int
    R_EF: int 
    RM_LADPerfusion: float
    RSD_LADPerfusion: float
    RM_LCXPerfusion: float
    RSD_LCXPerfusion: float
    RM_RCAPerfusion: float
    RSD_RCAPerfusion: float
    RM_TOTPerfusion: float
    RSD_TOTPerfusion: float
    RM_LADWallThickening: float
    RSD_LADWallThickening: float
    RM_LCXWallThickening: float
    RSD_LCXWallThickening: float
    RM_RCAWallThickening: float
    RSD_RCAWallThickening: float
    RM_TOTWallThickening: float
    RSD_TOTWallThickening: float
    RM_LADWallMotion: float
    RSD_LADWallMotion: float
    RM_LCXWallMotion: float
    RSD_LCXWallMotion: float
    RM_RCAWallMotion: float
    RSD_RCAWallMotion: float
    RM_TOTWallMotion: float
    RSD_TOTWallMotion: float    
    RE_LADPerfusion: int
    RE_LCXPerfusion: int
    RE_RCAPerfusion: int
    RE_TOTPerfusion: int
    RE_LADWallThickening: int
    RE_LCXWallThickening: int
    RE_RCAWallThickening: int
    RE_TOTWallThickening: int
    RE_LADWallMotion: int
    RE_LCXWallMotion: int
    RE_RCAWallMotion: int
    RE_TOTWallMotion: int
    RSEV_LADPerfusion: float
    RSEV_LCXPerfusion: float
    RSEV_RCAPerfusion: float
    RSEV_TOTPerfusion: float
    RSEV_LADWallThickening: float
    RSEV_LCXWallThickening: float
    RSEV_RCAWallThickening: float
    RSEV_TOTWallThickening: float
    RSEV_LADWallMotion: float
    RSEV_LCXWallMotion: float
    RSEV_RCAWallMotion: float
    RSEV_TOTWallMotion: float   
    SSS: int
    S_STS: int
    S_SMS: int
    SRS: int
    R_STS: int
    R_SMS: int
    age: int
    gender: str
    bmi: float
    dm: int
    ht: int
    dlp: int
    ckd: int

#----------------------------------------------------------------------



    @classmethod
    def as_form(cls, sepal_length: float = Form(...), sepal_width: float = Form(...), petal_length: float = Form(...), petal_width: float = Form(...)):
        return cls(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length, petal_width=petal_width)

    @classmethod
    def as_form(cls, patient_id: int = Form(...),
        S_MaxPerfusion: int = Form(...),
        S_Intervals: int = Form(...),
        S_ED: int = Form(...),
        S_ES: int = Form(...),
        S_EF: int = Form(...),   
        SM_LADPerfusion: float = Form(...),
        SSD_LADPerfusion: float = Form(...),
        SM_LCXPerfusion: float = Form(...),
        SSD_LCXPerfusion: float = Form(...),
        SM_RCAPerfusion: float = Form(...),
        SSD_RCAPerfusion: float = Form(...),
        SM_TOTPerfusion: float = Form(...),
        SSD_TOTPerfusion: float = Form(...),
        SM_LADWallThickening: float = Form(...),
        SSD_LADWallThickening: float = Form(...),
        SM_LCXWallThickening: float = Form(...),
        SSD_LCXWallThickening: float = Form(...),
        SM_RCAWallThickening: float = Form(...),
        SSD_RCAWallThickening: float = Form(...),
        SM_TOTWallThickening: float = Form(...),
        SSD_TOTWallThickening: float = Form(...),
        SM_LADWallMotion: float = Form(...),
        SSD_LADWallMotion: float = Form(...),
        SM_LCXWallMotion: float = Form(...),
        SSD_LCXWallMotion: float = Form(...),
        SM_RCAWallMotion: float = Form(...),
        SSD_RCAWallMotion: float = Form(...),
        SM_TOTWallMotion: float = Form(...),
        SSD_TOTWallMotion: float = Form(...),       
        SE_LADPerfusion: int = Form(...),
        SE_LCXPerfusion: int = Form(...),
        SE_RCAPerfusion: int = Form(...),
        SE_TOTPerfusion: int = Form(...),
        SE_LADWallThickening: int = Form(...),
        SE_LCXWallThickening: int = Form(...),
        SE_RCAWallThickening: int = Form(...),
        SE_TOTWallThickening: int = Form(...),
        SE_LADWallMotion: int = Form(...),
        SE_LCXWallMotion: int = Form(...),
        SE_RCAWallMotion: int = Form(...),
        SE_TOTWallMotion: int = Form(...),
        SSEV_LADPerfusion: float = Form(...),
        SSEV_LCXPerfusion: float = Form(...),
        SSEV_RCAPerfusion: float = Form(...),
        SSEV_TOTPerfusion: float = Form(...),
        SSEV_LADWallThickening: float = Form(...),
        SSEV_LCXWallThickening: float = Form(...),
        SSEV_RCAWallThickening: float = Form(...),
        SSEV_TOTWallThickening: float = Form(...),
        SSEV_LADWallMotion: float = Form(...),
        SSEV_LCXWallMotion: float = Form(...),
        SSEV_RCAWallMotion: float = Form(...),
        SSEV_TOTWallMotion: float = Form(...),
        R_MaxPerfusion: int = Form(...),
        R_Intervals: int = Form(...),
        R_ED: int = Form(...),
        R_ES: int = Form(...),
        R_EF: int = Form(...), 
        RM_LADPerfusion: float = Form(...),
        RSD_LADPerfusion: float = Form(...),
        RM_LCXPerfusion: float = Form(...),
        RSD_LCXPerfusion: float = Form(...),
        RM_RCAPerfusion: float = Form(...),
        RSD_RCAPerfusion: float = Form(...),
        RM_TOTPerfusion: float = Form(...),
        RSD_TOTPerfusion: float = Form(...),
        RM_LADWallThickening: float = Form(...),
        RSD_LADWallThickening: float = Form(...),
        RM_LCXWallThickening: float = Form(...),
        RSD_LCXWallThickening: float = Form(...),
        RM_RCAWallThickening: float = Form(...),
        RSD_RCAWallThickening: float = Form(...),
        RM_TOTWallThickening: float = Form(...),
        RSD_TOTWallThickening: float = Form(...),
        RM_LADWallMotion: float = Form(...),
        RSD_LADWallMotion: float = Form(...),
        RM_LCXWallMotion: float = Form(...),
        RSD_LCXWallMotion: float = Form(...),
        RM_RCAWallMotion: float = Form(...),
        RSD_RCAWallMotion: float = Form(...),
        RM_TOTWallMotion: float = Form(...),
        RSD_TOTWallMotion: float   = Form(...),  
        RE_LADPerfusion: int = Form(...),
        RE_LCXPerfusion: int = Form(...),
        RE_RCAPerfusion: int = Form(...),
        RE_TOTPerfusion: int = Form(...),
        RE_LADWallThickening: int = Form(...),
        RE_LCXWallThickening: int = Form(...),
        RE_RCAWallThickening: int = Form(...),
        RE_TOTWallThickening: int = Form(...),
        RE_LADWallMotion: int = Form(...),
        RE_LCXWallMotion: int = Form(...),
        RE_RCAWallMotion: int = Form(...),
        RE_TOTWallMotion: int = Form(...),
        RSEV_LADPerfusion: float = Form(...),
        RSEV_LCXPerfusion: float = Form(...),
        RSEV_RCAPerfusion: float = Form(...),
        RSEV_TOTPerfusion: float = Form(...),
        RSEV_LADWallThickening: float = Form(...),
        RSEV_LCXWallThickening: float = Form(...),
        RSEV_RCAWallThickening: float = Form(...),
        RSEV_TOTWallThickening: float = Form(...),
        RSEV_LADWallMotion: float = Form(...),
        RSEV_LCXWallMotion: float = Form(...),
        RSEV_RCAWallMotion: float = Form(...),
        RSEV_TOTWallMotion: float = Form(...),   
        SSS: int = Form(...),
        S_STS: int = Form(...),
        S_SMS: int = Form(...),
        SRS: int = Form(...),
        R_STS: int = Form(...),
        R_SMS: int = Form(...),
        age: int = Form(...),
        gender: str = Form(...),
        bmi: float = Form(...),
        dm: int = Form(...),
        ht: int = Form(...),
        dlp: int = Form(...),
        ckd: int = Form(...)): 
        return cls(patient_id = patient_id,
        S_MaxPerfusion=S_MaxPerfusion,
        S_Intervals = S_Intervals,
        S_ED = S_ED,
        S_ES = S_ES,
        S_EF = S_EF,   
        SM_LADPerfusion = SM_LADPerfusion,
        SSD_LADPerfusion = SSD_LADPerfusion,
        SM_LCXPerfusion = SM_LCXPerfusion,
        SSD_LCXPerfusion = SSD_LCXPerfusion,
        SM_RCAPerfusion = SM_RCAPerfusion,
        SSD_RCAPerfusion = SSD_RCAPerfusion,
        SM_TOTPerfusion = SM_TOTPerfusion,
        SSD_TOTPerfusion = SSD_TOTPerfusion,
        SM_LADWallThickening = SM_LADWallThickening,
        SSD_LADWallThickening = SSD_LADWallThickening,
        SM_LCXWallThickening = SM_LCXWallThickening,
        SSD_LCXWallThickening = SSD_LCXWallThickening,
        SM_RCAWallThickening = SM_RCAWallThickening,
        SSD_RCAWallThickening = SSD_RCAWallThickening,
        SM_TOTWallThickening = SM_TOTWallThickening,
        SSD_TOTWallThickening = SSD_TOTWallThickening,
        SM_LADWallMotion = SM_LADWallMotion,
        SSD_LADWallMotion = SSD_LADWallMotion,
        SM_LCXWallMotion = SM_LCXWallMotion,
        SSD_LCXWallMotion = SSD_LCXWallMotion,
        SM_RCAWallMotion = SM_RCAWallMotion,
        SSD_RCAWallMotion = SSD_RCAWallMotion,
        SM_TOTWallMotion = SM_TOTWallMotion,
        SSD_TOTWallMotion = SSD_TOTWallMotion,       
        SE_LADPerfusion = SE_LADPerfusion,
        SE_LCXPerfusion = SE_LCXPerfusion,
        SE_RCAPerfusion = SE_RCAPerfusion,
        SE_TOTPerfusion = SE_TOTPerfusion,
        SE_LADWallThickening = SE_LADWallThickening,
        SE_LCXWallThickening = SE_LCXWallThickening,
        SE_RCAWallThickening = SE_RCAWallThickening,
        SE_TOTWallThickening = SE_TOTWallThickening,
        SE_LADWallMotion = SE_LADWallMotion,
        SE_LCXWallMotion = SE_LCXWallMotion,
        SE_RCAWallMotion = SE_RCAWallMotion,
        SE_TOTWallMotion = SE_TOTWallMotion,
        SSEV_LADPerfusion = SSEV_LADPerfusion,
        SSEV_LCXPerfusion = SSEV_LCXPerfusion,
        SSEV_RCAPerfusion = SSEV_RCAPerfusion,
        SSEV_TOTPerfusion = SSEV_TOTPerfusion,
        SSEV_LADWallThickening = SSEV_LADWallThickening,
        SSEV_LCXWallThickening = SSEV_LCXWallThickening,
        SSEV_RCAWallThickening = SSEV_RCAWallThickening,
        SSEV_TOTWallThickening = SSEV_TOTWallThickening,
        SSEV_LADWallMotion = SSEV_LADWallMotion,
        SSEV_LCXWallMotion = SSEV_LCXWallMotion,
        SSEV_RCAWallMotion = SSEV_RCAWallMotion,
        SSEV_TOTWallMotion = SSEV_TOTWallMotion,
        R_MaxPerfusion = R_MaxPerfusion,
        R_Intervals = R_Intervals,
        R_ED = R_ED,
        R_ES = R_ES,
        R_EF = R_EF, 
        RM_LADPerfusion = RM_LADPerfusion,
        RSD_LADPerfusion = RSD_LADPerfusion,
        RM_LCXPerfusion = RM_LCXPerfusion,
        RSD_LCXPerfusion = RSD_LCXPerfusion,
        RM_RCAPerfusion = RM_RCAPerfusion,
        RSD_RCAPerfusion = RSD_RCAPerfusion,
        RM_TOTPerfusion = RM_TOTPerfusion,
        RSD_TOTPerfusion = RSD_TOTPerfusion,
        RM_LADWallThickening = RM_LADWallThickening,
        RSD_LADWallThickening = RSD_LADWallThickening,
        RM_LCXWallThickening = RM_LCXWallThickening,
        RSD_LCXWallThickening = RSD_LCXWallThickening,
        RM_RCAWallThickening = RM_RCAWallThickening,
        RSD_RCAWallThickening = RSD_RCAWallThickening,
        RM_TOTWallThickening = RM_TOTWallThickening,
        RSD_TOTWallThickening = RSD_TOTWallThickening,
        RM_LADWallMotion = RM_LADWallMotion,
        RSD_LADWallMotion = RSD_LADWallMotion,
        RM_LCXWallMotion = RM_LCXWallMotion,
        RSD_LCXWallMotion = RSD_LCXWallMotion,
        RM_RCAWallMotion = RM_RCAWallMotion,
        RSD_RCAWallMotion = RSD_RCAWallMotion,
        RM_TOTWallMotion = RM_TOTWallMotion,
        RSD_TOTWallMotion = RSD_TOTWallMotion,  
        RE_LADPerfusion = RE_LADPerfusion,
        RE_LCXPerfusion = RE_LCXPerfusion,
        RE_RCAPerfusion = RE_RCAPerfusion,
        RE_TOTPerfusion = RE_TOTPerfusion,
        RE_LADWallThickening = RE_LADWallThickening,
        RE_LCXWallThickening = RE_LCXWallThickening,
        RE_RCAWallThickening = RE_RCAWallThickening,
        RE_TOTWallThickening = RE_TOTWallThickening,
        RE_LADWallMotion = RE_LADWallMotion,
        RE_LCXWallMotion = RE_LCXWallMotion,
        RE_RCAWallMotion = RE_RCAWallMotion,
        RE_TOTWallMotion = RE_TOTWallMotion,
        RSEV_LADPerfusion = RSEV_LADPerfusion,
        RSEV_LCXPerfusion = RSEV_LCXPerfusion,
        RSEV_RCAPerfusion = RSEV_RCAPerfusion,
        RSEV_TOTPerfusion = RSEV_TOTPerfusion,
        RSEV_LADWallThickening = RSEV_LADWallThickening,
        RSEV_LCXWallThickening = RSEV_LCXWallThickening,
        RSEV_RCAWallThickening = RSEV_RCAWallThickening,
        RSEV_TOTWallThickening = RSEV_TOTWallThickening,
        RSEV_LADWallMotion = RSEV_LADWallMotion,
        RSEV_LCXWallMotion = RSEV_LCXWallMotion,
        RSEV_RCAWallMotion = RSEV_RCAWallMotion,
        RSEV_TOTWallMotion = RSEV_TOTWallMotion,   
        SSS = SSS,
        S_STS = S_STS,
        S_SMS = S_SMS,
        SRS = SRS,
        R_STS = R_STS,
        R_SMS = R_SMS,
        age = age,
        gender = gender,
        bmi = bmi,
        dm = dm,
        ht = ht,
        dlp = dlp,
        ckd = ckd)

class patient_schema_ocr(BaseModel):
    S_MaxPerfusion: int = Field(...)
    S_Intervals: int = Field(...)
    S_ED: int = Field(...)
    S_ES: int = Field(...)
    S_EF: int = Field(...)   
    SM_LADPerfusion: float = Field(...)
    SSD_LADPerfusion: float = Field(...)
    SM_LCXPerfusion: float = Field(...)
    SSD_LCXPerfusion: float = Field(...)
    SM_RCAPerfusion: float = Field(...)
    SSD_RCAPerfusion: float = Field(...)
    SM_TOTPerfusion: float = Field(...)
    SSD_TOTPerfusion: float = Field(...)
    SM_LADWallThickening: float = Field(...)
    SSD_LADWallThickening: float = Field(...)
    SM_LCXWallThickening: float = Field(...)
    SSD_LCXWallThickening: float = Field(...)
    SM_RCAWallThickening: float = Field(...)
    SSD_RCAWallThickening: float = Field(...)
    SM_TOTWallThickening: float = Field(...)
    SSD_TOTWallThickening: float = Field(...)
    SM_LADWallMotion: float = Field(...)
    SSD_LADWallMotion: float = Field(...)
    SM_LCXWallMotion: float = Field(...)
    SSD_LCXWallMotion: float = Field(...)
    SM_RCAWallMotion: float = Field(...)
    SSD_RCAWallMotion: float = Field(...)
    SM_TOTWallMotion: float = Field(...)
    SSD_TOTWallMotion: float = Field(...)      
    SE_LADPerfusion: int = Field(...)
    SE_LCXPerfusion: int = Field(...)
    SE_RCAPerfusion: int = Field(...)
    SE_TOTPerfusion: int = Field(...)
    SE_LADWallThickening: int = Field(...)
    SE_LCXWallThickening: int = Field(...)
    SE_RCAWallThickening: int = Field(...)
    SE_TOTWallThickening: int = Field(...)
    SE_LADWallMotion: int = Field(...)
    SE_LCXWallMotion: int = Field(...)
    SE_RCAWallMotion: int = Field(...)
    SE_TOTWallMotion: int = Field(...)
    SSEV_LADPerfusion: float = Field(...)
    SSEV_LCXPerfusion: float = Field(...)
    SSEV_RCAPerfusion: float = Field(...)
    SSEV_TOTPerfusion: float = Field(...)
    SSEV_LADWallThickening: float = Field(...)
    SSEV_LCXWallThickening: float = Field(...)
    SSEV_RCAWallThickening: float = Field(...)
    SSEV_TOTWallThickening: float = Field(...)
    SSEV_LADWallMotion: float = Field(...)
    SSEV_LCXWallMotion: float = Field(...)
    SSEV_RCAWallMotion: float = Field(...)
    SSEV_TOTWallMotion: float = Field(...)
    R_MaxPerfusion: int = Field(...)
    R_Intervals: int = Field(...)
    R_ED: int = Field(...)
    R_ES: int = Field(...)
    R_EF: int = Field(...) 
    RM_LADPerfusion: float = Field(...)
    RSD_LADPerfusion: float = Field(...)
    RM_LCXPerfusion: float = Field(...)
    RSD_LCXPerfusion: float = Field(...)
    RM_RCAPerfusion: float = Field(...)
    RSD_RCAPerfusion: float = Field(...)
    RM_TOTPerfusion: float = Field(...)
    RSD_TOTPerfusion: float = Field(...)
    RM_LADWallThickening: float = Field(...)
    RSD_LADWallThickening: float = Field(...)
    RM_LCXWallThickening: float = Field(...)
    RSD_LCXWallThickening: float = Field(...)
    RM_RCAWallThickening: float = Field(...)
    RSD_RCAWallThickening: float = Field(...)
    RM_TOTWallThickening: float = Field(...)
    RSD_TOTWallThickening: float = Field(...)
    RM_LADWallMotion: float = Field(...)
    RSD_LADWallMotion: float = Field(...)
    RM_LCXWallMotion: float = Field(...)
    RSD_LCXWallMotion: float = Field(...)
    RM_RCAWallMotion: float = Field(...)
    RSD_RCAWallMotion: float = Field(...)
    RM_TOTWallMotion: float = Field(...)
    RSD_TOTWallMotion: float   = Field(...)  
    RE_LADPerfusion: int = Field(...)
    RE_LCXPerfusion: int = Field(...)
    RE_RCAPerfusion: int = Field(...)
    RE_TOTPerfusion: int = Field(...)
    RE_LADWallThickening: int = Field(...)
    RE_LCXWallThickening: int = Field(...)
    RE_RCAWallThickening: int = Field(...)
    RE_TOTWallThickening: int = Field(...)
    RE_LADWallMotion: int = Field(...)
    RE_LCXWallMotion: int = Field(...)
    RE_RCAWallMotion: int = Field(...)
    RE_TOTWallMotion: int = Field(...)
    RSEV_LADPerfusion: float = Field(...)
    RSEV_LCXPerfusion: float = Field(...)
    RSEV_RCAPerfusion: float = Field(...)
    RSEV_TOTPerfusion: float = Field(...)
    RSEV_LADWallThickening: float = Field(...)
    RSEV_LCXWallThickening: float = Field(...)
    RSEV_RCAWallThickening: float = Field(...)
    RSEV_TOTWallThickening: float = Field(...)
    RSEV_LADWallMotion: float = Field(...)
    RSEV_LCXWallMotion: float = Field(...)
    RSEV_RCAWallMotion: float = Field(...)
    RSEV_TOTWallMotion: float = Field(...)   
    SSS: int = Field(...)
    S_STS: int = Field(...)
    S_SMS: int = Field(...)
    SRS: int = Field(...)
    R_STS: int = Field(...)
    R_SMS: int = Field(...)
    age: int = Field(...)
    gender: str = Field(...)
    bmi: float = Field(...)
    dm: int = Field(...)
    ht: int = Field(...)
    dlp: int = Field(...)
    ckd: int = Field(...)


class ocr_patient_schema_dict(BaseModel):
    S_MaxPerfusion: int = Field(...)
    S_Intervals: int = Field(...)
    S_ED: int = Field(...)
    S_ES: int = Field(...)
    S_EF: int = Field(...)   
    SM_LADPerfusion: float = Field(...)
    SSD_LADPerfusion: float = Field(...)
    SM_LCXPerfusion: float = Field(...)
    SSD_LCXPerfusion: float = Field(...)
    SM_RCAPerfusion: float = Field(...)
    SSD_RCAPerfusion: float = Field(...)
    SM_TOTPerfusion: float = Field(...)
    SSD_TOTPerfusion: float = Field(...)
    SM_LADWallThickening: float = Field(...)
    SSD_LADWallThickening: float = Field(...)
    SM_LCXWallThickening: float = Field(...)
    SSD_LCXWallThickening: float = Field(...)
    SM_RCAWallThickening: float = Field(...)
    SSD_RCAWallThickening: float = Field(...)
    SM_TOTWallThickening: float = Field(...)
    SSD_TOTWallThickening: float = Field(...)
    SM_LADWallMotion: float = Field(...)
    SSD_LADWallMotion: float = Field(...)
    SM_LCXWallMotion: float = Field(...)
    SSD_LCXWallMotion: float = Field(...)
    SM_RCAWallMotion: float = Field(...)
    SSD_RCAWallMotion: float = Field(...)
    SM_TOTWallMotion: float = Field(...)
    SSD_TOTWallMotion: float = Field(...)      
    SE_LADPerfusion: int = Field(...)
    SE_LCXPerfusion: int = Field(...)
    SE_RCAPerfusion: int = Field(...)
    SE_TOTPerfusion: int = Field(...)
    SE_LADWallThickening: int = Field(...)
    SE_LCXWallThickening: int = Field(...)
    SE_RCAWallThickening: int = Field(...)
    SE_TOTWallThickening: int = Field(...)
    SE_LADWallMotion: int = Field(...)
    SE_LCXWallMotion: int = Field(...)
    SE_RCAWallMotion: int = Field(...)
    SE_TOTWallMotion: int = Field(...)
    SSEV_LADPerfusion: float = Field(...)
    SSEV_LCXPerfusion: float = Field(...)
    SSEV_RCAPerfusion: float = Field(...)
    SSEV_TOTPerfusion: float = Field(...)
    SSEV_LADWallThickening: float = Field(...)
    SSEV_LCXWallThickening: float = Field(...)
    SSEV_RCAWallThickening: float = Field(...)
    SSEV_TOTWallThickening: float = Field(...)
    SSEV_LADWallMotion: float = Field(...)
    SSEV_LCXWallMotion: float = Field(...)
    SSEV_RCAWallMotion: float = Field(...)
    SSEV_TOTWallMotion: float = Field(...)
    R_MaxPerfusion: int = Field(...)
    R_Intervals: int = Field(...)
    R_ED: int = Field(...)
    R_ES: int = Field(...)
    R_EF: int = Field(...) 
    RM_LADPerfusion: float = Field(...)
    RSD_LADPerfusion: float = Field(...)
    RM_LCXPerfusion: float = Field(...)
    RSD_LCXPerfusion: float = Field(...)
    RM_RCAPerfusion: float = Field(...)
    RSD_RCAPerfusion: float = Field(...)
    RM_TOTPerfusion: float = Field(...)
    RSD_TOTPerfusion: float = Field(...)
    RM_LADWallThickening: float = Field(...)
    RSD_LADWallThickening: float = Field(...)
    RM_LCXWallThickening: float = Field(...)
    RSD_LCXWallThickening: float = Field(...)
    RM_RCAWallThickening: float = Field(...)
    RSD_RCAWallThickening: float = Field(...)
    RM_TOTWallThickening: float = Field(...)
    RSD_TOTWallThickening: float = Field(...)
    RM_LADWallMotion: float = Field(...)
    RSD_LADWallMotion: float = Field(...)
    RM_LCXWallMotion: float = Field(...)
    RSD_LCXWallMotion: float = Field(...)
    RM_RCAWallMotion: float = Field(...)
    RSD_RCAWallMotion: float = Field(...)
    RM_TOTWallMotion: float = Field(...)
    RSD_TOTWallMotion: float   = Field(...)  
    RE_LADPerfusion: int = Field(...)
    RE_LCXPerfusion: int = Field(...)
    RE_RCAPerfusion: int = Field(...)
    RE_TOTPerfusion: int = Field(...)
    RE_LADWallThickening: int = Field(...)
    RE_LCXWallThickening: int = Field(...)
    RE_RCAWallThickening: int = Field(...)
    RE_TOTWallThickening: int = Field(...)
    RE_LADWallMotion: int = Field(...)
    RE_LCXWallMotion: int = Field(...)
    RE_RCAWallMotion: int = Field(...)
    RE_TOTWallMotion: int = Field(...)
    RSEV_LADPerfusion: float = Field(...)
    RSEV_LCXPerfusion: float = Field(...)
    RSEV_RCAPerfusion: float = Field(...)
    RSEV_TOTPerfusion: float = Field(...)
    RSEV_LADWallThickening: float = Field(...)
    RSEV_LCXWallThickening: float = Field(...)
    RSEV_RCAWallThickening: float = Field(...)
    RSEV_TOTWallThickening: float = Field(...)
    RSEV_LADWallMotion: float = Field(...)
    RSEV_LCXWallMotion: float = Field(...)
    RSEV_RCAWallMotion: float = Field(...)
    RSEV_TOTWallMotion: float = Field(...)   
    SSS: int = Field(...)
    S_STS: int = Field(...)
    S_SMS: int = Field(...)
    SRS: int = Field(...)
    R_STS: int = Field(...)
    R_SMS: int = Field(...)
    age: int = Field(...)
    gender: str = Field(...)
    bmi: float = Field(...)
    dm: int = Field(...)
    ht: int = Field(...)
    dlp: int = Field(...)
    ckd: int = Field(...)

class inference_ocr_schema(BaseModel):
    values: list = Field(...)
    patient_characteristic: dict = Field(...)



