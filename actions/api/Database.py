# ---------- INSTALLATION REQUIREMENTS ---------- #
'''
    py -m pip install "pymongo[srv]"==3.6
    pip install python-dotenv
'''
# ---------- INSTALLATION REQUIREMENTS ---------- #

# ---------- SECURE APIs AND IDs ---------- #
from typing import Final
from dotenv import load_dotenv
import os

load_dotenv()

# Load the hidden environment variables
URI: Final = os.getenv("URI")    


# ---------- SECURE API TOKEN ---------- #

# ---------- DATABASE SETUP ---------- #

from pymongo.mongo_client import MongoClient

class Database:
    # creates and connects the local database
    def __init__(self):
        self.client = MongoClient(URI)
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        self.db = self.client.get_database('chatbot')
        self.responses = self.db.responses

    def get_sample_response(self):
        response = self.responses.find_one({'utter': 'greeting'})
        if response:
            return response.get('text')
        else:
            return "Response does not exist."
         
# # ---------- DATABASE SETUP ---------- #