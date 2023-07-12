import requests
import json
url = 'https://api.ai21.com/studio/v1/j2-ultra/complete'

headers = {
    'content-type' : 'application/json',
    'authorization' : 'Bearer '
}

payload = {
    "prompt" : "simplify the jargon : The fund managers hope to increase yields by taking on leverage.",
    "numResults":1,
  "maxTokens":40,
  "temperature":0.4,
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
  },
    "stopSequences":["Jargon:","↵↵"]
}

response = requests.post(url, json=payload, headers=headers)
# print(type(response.text))
js = json.loads(response.text)
print(js['completions'][0]['data']['text'])