import os

from dotenv import load_dotenv

load_dotenv()

allowed_users = [1865314469,]

IMEI_TOKEN = os.getenv('IMEI_TOKEN')
API_TOKEN = os.getenv("API_TOKEN")
BOT_TOKEN = os.getenv('BOT_TOKEN')

API_URL = "http://localhost:8000/api/check-imei"