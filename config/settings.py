import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL_UI = "https://www.imdb.com"
BASE_URL_API = "https://api.poiskkino.dev/v1.4"
API_KEY = os.getenv("POISKKINO_API_KEY", "HW01WCP-0FY4TBZ-QVCKJNC-NN46R8M")