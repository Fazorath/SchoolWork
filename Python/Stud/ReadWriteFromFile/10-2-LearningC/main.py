path = "CodingJourney/Python/Studying/Reading/10-1-LearningPython/learning.txt"

## 10-2 Using replace in a file
with open(path,'r') as f:
  content = f.readlines()
  for line in content:
    line = line.strip().replace('python','replaced')
    print(line)    
