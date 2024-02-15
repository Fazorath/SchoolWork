## Yoenis Hernandez
## 12/31/2018
## The goal for this program is to take a CSV file and create JSON strings that can be used in JavaScript 
## for each row of data that is not the header row.  JavaScript is a scripting language used for web pages.  
## JSON is a common format used to transmit data for web apps from a web server to a client 
## (i.e. such as from sfcollege.edu's web server to your computer) so it can be displayed in a browser.
## Create a class and FN
## Read a CSV
## Keep CSV header
## Paid header with the values
## Ceate Json String
## Return JSON string to Screen
## return JSON string to file
import json

def opencsv():
    filename="/Users/exempt/Repo Codespace/CodingJourney/Python/Project7/Project7TestFile.csv"
    # input("Enter the file Name: ")
    with open(filename, 'r') as file:
        filelines = file.readlines()
        headers = filelines[0].strip().split(',')
        print(headers)
        JsonData = []
        for line in filelines[1:]:
            values = line.strip().split(',')
            row = dict(zip(headers, values))
            JsonData.append(row)
        print(JsonData)
            

def splitcsv(content):
    for item in content:
        data = item.split(',')
        print('\n')
        print(data)
    return data


def main():
    content = opencsv()
    

if __name__ == "__main__":
    main()


# 1. Open csv file
# 2. Read csv file 
# 3. Create JSON strings
# 4. Write JSON strings to a file

