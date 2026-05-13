from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Set a timeout so the app doesn't hang forever if DB is down
client = MongoClient(os.getenv("MONGO_URL"), serverSelectionTimeoutMS=5000)

db = client["finance_ai"]

collection = db["finance_records"]