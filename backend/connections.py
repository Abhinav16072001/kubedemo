from pymongo import MongoClient
import os

# Fetch MongoDB URI and database name from environment variables (recommended)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "demo")

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    coll = db["names"]
    print("✅ MongoDB connection established successfully.")
except Exception as e:
    print(f"❌ Failed to connect to MongoDB: {e}")
