import json

favnum = int(input("What is your Favorite Number: "))
## write to the json file
path = 'CodingJourney/Python/Studying/Reading/Txts/numbers.json'
with open(path,'w') as f:
  json.dump(favnum,f)

## read from the json file
with open(path) as f:
  number = json.load(f)
  print(f"Your favorite number is: {number} !!")