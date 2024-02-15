path = "CodingJourney/Python/Studying/Reading/Texts/Example.txt"

## Reading the file
with open(path) as f:
    content = f.read()
    print(content)
  
## Reading the file line by line
with open(path) as f:
    linecontent = f.readlines() # Displays the Forward slash n/ CREATES A LIST 
    print(linecontent)

# To remove the Forward slash n
with open(path) as f:
    linecontent = f.readlines() # Displays the Forward slash n 
    for line in linecontent:
        line = line.rstrip()
        print(line)