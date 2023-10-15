# Dictionary of programming terms and their definitions
programming_terms = {
    1: ("Algorithm", "is a set of instructions that are followed to solve a problem."),
    2: ("Variable", "container that holds a single number, word, or other information that you can use throughout a program."),
    3: ("Variable Type (data type)", "Basic variable types include: string (words and phrases), char (short for 'character;' a single letter or symbol you can type), int (short for 'integer;' for whole numbers), double or float (for decimal numbers), and bool (short for 'boolean;' for true or false values."),
    4: ("Array", "containers that hold variables of the same data type."),
    5: ("If statement", "runs a block of code based on whether or not a condition is true."),
    6: ("Loop","check a condition and then run a code block.  The loop will continue to check and run until a specified condition is reached."),
    7: ("Function","block of code that can be referenced by name to run the code it contains."),
    8: ("Class","template definition of the methods and variables in a particular kind of object."),
    9: ("Object","data type that has unique attributes and behavior."),
    10: ("Method","programmed procedure that is defined as part of a class and is available to any object instantiated from that class."),
    11: ("Programming Language","system of notation for writing computer programs.  Python is an example."),
    12: ("Control Structure","basic blocks for decision making processes in computing."),
    13: ("Error!","Not a valid choice."),
}

# Function to display the menu and provide definitions
def display_menu():
    print("This program will provide definitions to important programming terms.")
    print("Choose a number to see the term's definition.\n")
    print("Terms:")
    for key, value in programming_terms.items():
        if key > 12:
            break
        print(f"{key}: {value[0]}")
    try: 
        player = int(input(f"\nEnter the number of the term you want to learn about :"))
        if player in programming_terms:
            term, definition = programming_terms[player]
            print(f"\n{term}: {definition}\n")
        elif player not in programming_terms:
            term, definition = programming_terms[13]
            print(f"\n{term} {definition}\n")
        elif player == str(programming_terms):
            term, definition = programming_terms[13]
            print(f"\n{term} {definition}\n")
    except ValueError:
        player == str(programming_terms)
        term, definition = programming_terms[13]
        print(f"\n{term} {definition}\n")
        
        
# Main program loop
if __name__ == "__main__":
    display_menu()