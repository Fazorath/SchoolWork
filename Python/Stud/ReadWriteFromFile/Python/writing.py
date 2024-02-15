## Writing to a file using the 'w' mode
## When writing a file remember to use \n for new written lines
path = "CodingJourney/Python/Studying/Reading/Texts/empty.txt"
with open(path,'w') as file:
  file.write("first time writing into a file\n")
  file.write("Including a 2nd write statement without")