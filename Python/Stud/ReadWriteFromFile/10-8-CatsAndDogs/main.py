try:
  with open('CodingJourney/Python/Studying/Reading/10-8-CatsAndDogs/cats.txt') as f:
    contentcat = f.read()
  with open('CodingJourney/Python/Studying/Reading/10-8-CatsAndDogs/dogs.txt') as f:
    contentdog = f.read()
except FileNotFoundError:
  print(f"File not Found")
else:
  print(contentcat)
  print("\n")
  print(contentdog)