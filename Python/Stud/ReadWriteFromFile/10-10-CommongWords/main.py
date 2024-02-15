path = 'CodingJourney/Python/Studying/Reading/10-10-CommongWords/dracula.txt'
# How many times does the word the show up in the text?
with open(path, 'r') as file:
  content = file.read()
print(f"The word 'the' shows up: {content.count('the')} times")
## the with the space
print(f"The word 'the ' shows up: {content.count('the ')} times")
