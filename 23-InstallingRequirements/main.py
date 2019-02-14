import requests

API_URL = "https://cat-fact.herokuapp.com/facts/random"

response = requests.get(API_URL).json()

print(response["text"])
