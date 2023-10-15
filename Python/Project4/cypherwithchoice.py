## Yoenis Hernanez
## COP 2002 0.M2
## OCT 6, 2023
## Last updated Oct 9, 2023
##  -Figured out the proper output formatting at the ITE Lab.
## Ceasar Cypher using 2 lists and a for loop that identifies the index of the user input against
## StartingLetters and assigns that index to the modified letters lists since they are the same lists just shifted.
## these modified letters are then printed and concotanated into a variable and printed out.
## I cant figure out how to create different shifts because i am not sure how to implement them in the index if it can be reviewed in lectures
## only way i thought of was creating multiple modified alphabet lists for each shift up to a certain number but too bulky.
## and i also know that a while loop is probably more efficient but i cannot seem to get it to work.

## 2 lists. One is going to be used for the starting index
## Second list is going to be used for the index of the shifted user input 
StartingLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ModifiedLetters = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",  "t", "u", "v", "w", "x", "y", "z", "a"]

## User input that is going to be Encrypted
UserInp = input("Enter your text: ")

# The encrypted text will be placed in this variable
EncryptedText = " "

#For loop
for letter in UserInp: # Creating a variable for every letter in user input
    if letter in StartingLetters:  # if the letter is in my Starting list
        index = StartingLetters.index(letter)  # Assign the index of the input letters to Startingletters list
        encrypted = ModifiedLetters[index]  # Variable with the index of the letters but using the Modified letters list
        EncryptedText += encrypted  # Variable above is added to previous result variable
    else: 
        EncryptedText += letter # To handle if user input anything other than in Starting List 
print(EncryptedText) # Print final message
