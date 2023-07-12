import requests
import ast
import dotenv
import os
import json

dotenv.load_dotenv('.env')
bearer = os.getenv('api')

url = "https://api.ai21.com/studio/v1/gec"

input_text = input("input a paragraph to summarize : ")

payload = {
    # "sourceType": "TEXT",
    "source": input_text
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": f"Bearer {bearer}"
}

response = requests.post(url, json=payload, headers=headers)

# print((response.text))
rep = json.loads(response.text)
print(rep)