path = 'CodingJourney/Python/Studying/Reading/10-1-LearningPython/learning.txt'

# The whole File
print("Read the whole file\n")
with open(path) as f:
    content = f.read()
    print(content)

# line By line
print("\nRead line by line using for and Dictionary\n")
with open(path) as f:
    for line in f:
        line = line.rstrip()
        print(line)

print(f"\nLine by line using a list\n")
with open(path) as f:
    listcontent = f.readlines()
    print(listcontent[0].strip())
    print(listcontent[1].strip())
    print(listcontent[2].strip())
    print(listcontent[3].strip())
    print(listcontent[4].strip())