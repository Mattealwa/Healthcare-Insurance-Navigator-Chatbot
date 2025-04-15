from google.generativeai import GenerativeModel
from tools import load_insurance_data
import json
import os


model = GenerativeModel("gemini-1.5-pro")


insurance_data = load_insurance_data()


MEMORY_FILE = "user_memory.json"

def load_user_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {}

def save_user_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)
