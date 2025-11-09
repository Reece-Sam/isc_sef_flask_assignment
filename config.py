import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:Bonisamkk@localhost/bookdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False