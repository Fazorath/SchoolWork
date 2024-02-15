import json

path = 'CodingJourney/Python/Studying/Reading/Txts/numbers.json'

with open(path) as f:
  username = json.load(f)
  print(f"Welcome Back: {username}")
