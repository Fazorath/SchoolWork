import json
## Storing data using Json Module
## json.dump() and json.load()

numbers = [2, 3, 5, 7, 11, 13]
path = 'CodingJourney/Python/Studying/Reading/Txts/numbers.json'
with open(path, 'w') as f:
  json.dump(numbers, f)

## Reading the data back using json.load()
with open(path) as f:
  numbers = json.load(f)
  print(numbers)