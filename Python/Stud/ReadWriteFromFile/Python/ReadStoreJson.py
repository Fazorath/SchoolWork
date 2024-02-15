import json

username = input("What is your name? ")
path = 'CodingJourney/Python/Studying/Reading/Txts/numbers.json'

with open(path,'w') as f:
  json.dump(username,f)
  print(f"We will remember you when you come back: {username}")

