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