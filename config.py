import os
from dotenv import load_dotenv


load_dotenv()

# безопасно читаем переменные
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")


url = f"postgresql+psycopg://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{DB_NAME}"