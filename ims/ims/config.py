from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
print(os.getenv("DB_NAME"))

DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")