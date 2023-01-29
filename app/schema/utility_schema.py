from datetime import datetime
from pydantic import BaseModel
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Joe Doe",
                "email": "joe@xyz.com",
                "password": "any"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "joe@xyz.com",
                "password": "any"
            }
        }

class ocr_schema(BaseModel):
    hn: str = Field(...)
    client_root_path: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "hn": "048278-46",
                "client_root_path": "app/ocr/data_for_test/",
            }
        }