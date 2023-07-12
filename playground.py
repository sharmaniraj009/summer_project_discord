import requests


url = 'https://api.ai21.com/studio/v1/j2-ultra/complete'

headers = {
    'content-type: application/json'
    'authorization: Bearer '
}

payload = {
    "prompt":"give me information on ww2",
    "numResults":1,
    "maxTokens":1815,
    "temperature":0.7,
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
print(payload)

r = requests.post(url=url, json=payload, headers=headers)
print(r.text)