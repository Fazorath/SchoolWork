## Appending to a file using the 'a' mode
path = "CodingJourney/Python/Studying/Reading/Texts/empty.txt"

with open(path, "a") as file:
    file.write("\nThis is a new appended line")
    file.write("\nThis is another new appended line")
