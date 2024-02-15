# ## Handling Exceptions
# ## Handled using Try and Except blocks

# ## ZeroDivisionError
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# print("Give me 2 numbers, and ill divide them")
# print("Enter 'q' to quit")


# ## Incorporating ZeroDivisionError into a while loop
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number)/ int(second_number)
#     except ZeroDivisionError:
#         print("You cannot divide by 0")
#     else:
#         print(answer)


# ## FileNotFoundError
# path = 'alice.txt'

# try:
#     with open(path, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry File name:{path}File not found")

## Analyzing Text
def countwords(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()      
    except FileNotFoundError:
        print("file Not found")
    else:
    # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


path = 'CodingJourney/Python/Studying/Reading/Txts/alice.txt'
countwords(path)

## Multiple files in a list and uing a for loop to call the function
bookfiles = ['helloworld.txt','dune.txt','airplane.txt']
for file in bookfiles:
    countwords(file)

## Failing silently
try:
    print(5/0)
except ZeroDivisionError:
    pass
else:
    print("No errors found")
