from typing import  List
from celery import shared_task
from app.ocr import ocr_mpi
import pandas as pd

@shared_task( bind=True,autoretry_for=(Exception,), retry_backoff=True, rettry_kwargs={"max_retries": 5},  track_started=True, queue='extract_data', name='extract_data:ocr_extract_task')
def ocr_extract_task(self, hn: str, client_root_path: str):
    # Extract data
    extract_df, confidence_df, msg_error = ocr_mpi.main(client_root_path, hn)
    extract_df.replace({'-': '0'}, inplace=True) 

    result_extract = extract_df.values.tolist()[0]
    result_confidence = confidence_df.values.tolist()[0]
    concat_result = [[float(result_extract[i]), result_confidence[i]] for i in range(1, len(result_extract))]
    print("msg_error: ", msg_error)
    print("len(concat_result): ", len(concat_result))


    return concat_result


