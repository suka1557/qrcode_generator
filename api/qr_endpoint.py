from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from configs.config import BASE_URL
from src.qr_code_generator import generate_qr_code_with_data

qr_api = FastAPI()

#Define a Pydantic basemodel for kind of data expected in request body
class QRData(BaseModel):
    customer_id: str
    table_no: int
    url: Optional[str] = BASE_URL

@qr_api.post('/generate_qr_code')
def generate_qr(qr_data: QRData):
    return generate_qr_code_with_data(data_to_be_encoded=qr_data)
