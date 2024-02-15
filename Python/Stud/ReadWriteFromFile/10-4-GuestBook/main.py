path = "CodingJourney/Python/Studying/Reading/Texts/guests.txt"


## Loop that will ask for 10 names and write them to the file
counter = 0
while counter < 10:
  with open(path,'a') as file:
    name = input("What is your name? ")
    file.write(f"{name.title()}\n")
  counter += 1

