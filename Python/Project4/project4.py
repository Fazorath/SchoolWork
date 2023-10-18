## Yoenis Hernanez
## COP 2002 0.M2
## OCT 6, 2023
## Last updated Oct 9, 2023
## - Redid due to message in latest lecture about help. 
## - I showed up to the ITE student hours and recieved some help from the tutor
## - Rather be safe than sorry dont know if it counts 🤷🏻‍♂️ 
## ------------------------------------------------------------------------------------------------------------------
## Figured out the proper output formatting at the ITE Lab.
## Ceasar Cypher using 2 lists and a for loop that identifies the index of the user input against
## StartingLetters and assigns that index to the modified letters lists since they are the same lists just shifted.
## these modified letters are then printed and concotanated into a variable and printed out.
## I cant figure out how to create different shifts because i am not sure how to implement them in the index if it can be reviewed in lectures
## only way i thought of was creating multiple modified alphabet lists for each shift up to a certain number but too bulky.
## and i also know that a while loop is probably more efficient but i cannot seem to get it to work.


StartingLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ModifiedLetters = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",  "t", "u", "v", "w", "x", "y", "z", "a"]

def main():
  ## Get user Message
  userinput = input("Enter Text to encrypt: ")
  ## User input using list element
  userinputcopy = list(userinput) ## Copying list since pop Permanently changes it
  # return var
  cipher = ''
  # Go through each letter
  while userinputcopy:
    character = userinputcopy.pop(0)
    index = 0
    if character in StartingLetters: ## if the character is here add it
      while character != StartingLetters[index]:
        index += 1
    else: ## if character is not found add it to start list
      cipher += character
      continue ## while loop to keep going
    cipher += ModifiedLetters[index]
  print('Modified Message: ',cipher)
    

if __name__=="__main__":
  main()