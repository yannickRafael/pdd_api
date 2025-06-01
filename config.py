import os
from dotenv import load_dotenv

class Config:
    load_dotenv()
    DEBUG = os.environ.get('DEBUG') == 'True'
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')

    error_codes = {
        "E-AE": {
            "message": "Student Already Exists",
            "code": 409
        },
        "E-NOME-MP": {
            "message": "e_nome missing parameter",
            "code": 400
        },
        "E-CODE-MP": {
            "message": "e_code missing parameter",
            "code": 400
        },
        "E-ID-MP": {
            "message": "e_id missing parameter",
            "code": 400
        },
        "E-ID-NV": {
            "message": "e_id not valid",
            "code": 404
        },
        "CU-NOME-MP": {
            "message": "cu_nome missing parameter",
            "code": 400
        },
        "CU-CODE-MP": {
            "message": "cu_code missing parameter",
            "code": 400
        },
        "CU-ID-MP": {
            "message": "cu_id missing parameter",
            "code": 400
        },
        "CU-ID-NV": {
            "message": "cu_id not valid",
            "code": 404
        },
        "CU-AE": {
            "message": "Course Already Exists",
            "code": 409
        },
        "CA-AE": {
            "message": "Subject Already Exists",
            "code": 409
        },
    }

