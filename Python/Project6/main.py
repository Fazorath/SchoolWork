# Yoenis Hernandez
# COP 2002 0.M2
# 11/2/23
# Opening and writing to a CSV Project
# I went with the same approach as my last project of basically turning everything into functions and calling them in the main function
# i have 3 main functions that read from the files I opted to go for the bonus points so my answer 
# provided grabs the classes from the master file provided in Canvas
# I created 5 main functions 
# 1. readroster() reads the roster file provided and returns the list of appropriate codes
# 2. readcsvs() reads the master code file and returns the list of appropriate codes and names
# 3. readitems() displays the Codes that are being Read from roster CSV file all nice and purrty
# 4. incsv() if roster codes are in the master code files assign the class names to variable and return the list
# 5. writecsv() write the list created in last function onto a new file 
# https://github.com/Fazorath/CodingJourney/tree/main/Python/Project6



def readroster(file):  # reads the roster file and returns the list of appropriate codes
    with open(file, "r") as f:
        rostercodes = []  # initializes the list
        for line in f:
            columns = line.split(",")  # splits the line into columns
            code = columns[5].strip()  # gets the code from the 6th column
            rostercodes.append(code)  # adds the code to the list
        # removes the first item in the list needed to get read of the header
        rostercodes.pop(0)
        return rostercodes


def readcsvs(file1, column=0):  # reads the master code file and returns the list of appropriate codes/ this is actually the upgraded merged version i came up with
    # on the github is the first insane iteration with 3 functions
    with open(file1, "r") as f:
        codes = []
        for line in f:
            columns = line.split(",")
            # lets you choose whcih column as an argument. used to have a function for each column lol
            code = columns[column].strip()
            codes.append(code)
        return codes


def readitems(list):  # displays the Codes that are being Read from CSV file
    for item in list:
        print(f"*{item}*")  # Proper formatting like in the Screenshots


def incsv(master, roster, classes):   # if roster codes are in the master code files
    print("\tWriting to file...")
    correctclasses = []
    for item in roster:  # item in roster
        if item in master:  # if that item is in the master list
            # gets the index of the item in the master list and uses that index to get the class name from the class name list
            correctclass = (f'\t{classes[master.index(item)]}')
            correctclasses.append(correctclass)
    # needed to be returned to use as list to be written in writecsv function
    return correctclasses


def writecsv(file, items):  # the file path and the list needed to be written
    with open(file, "w") as f:
        for item in items:  # prints the list to the console
            print(f"\t{item}")
        for item in items:  # writes the list to the file
            f.write(f"{item}\n")


def main():
    # Welcome Message
    print("Processing Student input Files...")

    # My file paths
    path1 = "CodingJourney/Python/Project6/student roster example.csv"
    path2 = "CodingJourney/Python/Project6/Program Codes.csv"
    path3 = "CodingJourney/Python/Project6/output.csv"

    # Class Codes
    classroster = readroster(path1)

    # Master Codes From file list given
    mastercodes = readcsvs(path2, 0)

    # correct classes to be wrtten to file
    classname = readcsvs(path2, 1)

    # Displays the codes read from Student Roster
    readitems(classroster)
    print("\n")

    # Checks to see which codes from class roster are in the mastercodes list and adds the correct corresponding class to a list
    correctclass = incsv(mastercodes, classroster, classname)

    # Write function using the path to new file and the correct class list from above
    writecsv(path3, correctclass)

    # Completion Message
    print("\nProgram Completed!")


if __name__ == "__main__":
    main()
