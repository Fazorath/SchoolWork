path = "CodingJourney/Python/Studying/Reading/Texts/poll.txt"

while True:
  prompt = input("Why do you like programming? ")
  with open(path, "a") as file:
    file.write(f"{prompt}\n")