## Guest 10-3

path = "CodingJourney/Python/Studying/Reading/Texts/guests.txt"
name = input("What is your name? ")

with open(path,'a') as file:
  file.write(f"{name.title()}\n")

