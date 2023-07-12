import requests
import json
url = 'https://api.ai21.com/studio/v1/j2-light/complete'
# input_text = str(input())

headers = {
    'content-type' : 'application/json',
    'authorization' : f'Bearer '
}

payload = {
    "prompt" : "Article title on organizational trust",
    "numResults":1,
  "maxTokens":64,
  "temperature":0.85,
  "topKReturn": 0,
  "topP":1,
  "countPenalty": {
    "scale": 0,
    "applyToNumbers": False,
    "applyToPunctuations": False,
    "applyToStopwords": False,
    "applyToWhitespaces": False,
    "applyToEmojis": False
  },
  "frequencyPenalty": {
    "scale": 0,
    "applyToNumbers": False,
    "applyToPunctuations": False,
    "applyToStopwords": False,
    "applyToWhitespaces": False,
    "applyToEmojis": False
  },
  "presencePenalty": {
    "scale": 0,
    "applyToNumbers": False,
    "applyToPunctuations": False,
    "applyToStopwords": False,
    "applyToWhitespaces": False,
    "applyToEmojis": False
  }
}

response = requests.post(url, json=payload, headers=headers)
# print(type(response.text))
js = json.loads(response.text)
print(js['completions'][0]['data']['text'])