import json

path = 'CodingJourney/Python/Studying/Reading/Txts/numbers.json'

try:
  with open(path) as f:
    username = json.load(f)
except FileNotFoundError:
  username = input("What is your name? ")
  with open(path,'w') as f:
    json.dump(username,f)
else:
  print(f"Welcome Back: {username}")