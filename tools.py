import json

def load_insurance_data():
    with open("mock_data.json", "r") as file:
        data = json.load(file)
    return data
