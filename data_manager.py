import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

AUTH_KEY = os.getenv('SHEETY_AUTH_KEY')
AUTH_ENDPOINT = os.getenv('SHEETY_ENDPOINT')

class DataManager:
    def __init__(self):
        self.auth_headers = {
            'Authorization': f'Basic {AUTH_KEY}'
        }
        self.endpoint = AUTH_ENDPOINT
        self.data = None

        self.retrieve_data()

    def retrieve_data(self):
        response = requests.get(url=self.endpoint,headers=self.auth_headers)
        self.data = response.json()
        pprint(self.data)

