import json
path = 'CodingJourney/Python/Studying/Reading/Txts/numbers.json'

try:
  with open(path) as f:
    number = json.load(f)
except FileNotFoundError:
  favnum = int(input("What is your Favorite Number: "))
  with open(path,'w') as f:
    json.dump(favnum,f)
else:
  print(f"Your Favorite Number is: {number}")
  