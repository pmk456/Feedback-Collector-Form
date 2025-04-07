"""
Author Name: Patan Musthakheem
Date & Time: 08-04-2025 12:44 Am
File: db_handler.py
"""
from pymongo import MongoClient

import os

class DBHandler:
    def __init__(self):
        MONGO_URI = os.getenv("MONGO_URI")
        try:
            self.client = MongoClient(MONGO_URI)
            self.db = self.client['FeedbackDB']
            self.collection = self.db['feedback']
        except:
            raise
        
    def insert_record(self, data):
        try:
            self.collection.insert_one(data)
            return True
        except:
            return False
        
if __name__ == "__main__":
    handler = DBHandler()
    handler.insert_record({"Test": "Working"})
