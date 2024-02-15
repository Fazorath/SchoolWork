## Yoenis Hernandez
## 11/19/2023
## The goal for this program is to take a txt file and create JSON strings that can be used in JavaScript 
## for each row of data that is not the header row.  JavaScript is a scripting language used for web pages.  
## JSON is a common format used to transmit data for web apps from a web server to a client 
## (i.e. such as from sfcollege.edu's web server to your computer) so it can be displayed in a browser.
## Create a class and FN
## Read a txt 
## Keep CSV header
## Pair header with the values
## Create Json String
## Return JSON string to Screen
## return JSON string to file

class CSVtoJSON:
    def __init__(self):
        ## Source File Path
        self.filename = input("Enter the CSV file Name: ")
        ## Output File Path
        self.output_fileName = input("Enter the JSON file Name: ")
        ## Holds the Header row of the csv file
        self.header = []
        ## Holds the value of the source data
        self.read_filename = []
        ## Holds the JSON string
        self.data = []

    def read_txt_file(self):
      
        try: ## Exception handling
            with open(self.filename, "r") as f:
                file_read = []
                for line in f.readlines():
                    file_read.append(line.strip()) ## Reading the contents of the text file but stripped
        except:
            print(f"{self.filename} not found")
       
        else:
            self.read_filename = file_read ## Assigning the contents of the text file to the read_filename variable
            # print(file_read) ## Checks
  
    def assign_header(self): ## Assigns the header of the txt file
        self.header = self.read_filename[0].strip().split(",")  ## Strips the header of the txt file and splits it by the comma
        # print(self.read_filename[2]) ##checking to see if this could work to pair values together

    def pair_header_values(self): ## Pairs the header with the values of the txt file
        for line in self.read_filename[1:]: ## splits the contents of the txt file by the comma
            lines = line.split(",")
            # print(lines[3])
            row = {} ## Creates a dictionary
            for i in range(len(self.header)):
                row[self.header[i]] = lines[i] ## Assigns the header to the row
            self.data.append(row) ## Appends the row to the data variable previously created
        # print(self.data) ## Checks the data variable

    def create_json_string(self): ## Creates the JSON strings
        counter = 1 ## Counter for the JSON string
        ## Manually creating the json strings for each row
        json = "{" 
        for item in self.data: ## Loops through the data variable
            json += f'"{counter}":{{' ## Adds the counter to the json string
            for i in range(len(self.header)): ## Loops through the header variable
                key = self.header[i]
                value = item[key]
                if i == 2: ## this will get rid of the Quoatiations on the 2nd ID column
                    json += f'"{key}":{value}'
                elif i == 3: ## This will get rid of the quotations on the 3rd column and transforms to lowercase
                    json += f'"{key}":{value.lower()}'
                else:
                    json += f'"{key}":"{value}"' ## Adds the key and value to the json string
                if i < len(self.header) - 1: ## Adds a comma to the json string
                    json += "," 
            json += "}" ## Adds the closing curly brace
            if counter < len(self.data): 
                json += ","
            counter += 1 ## Increments the counter
        json += "}" ## Adds the closing curly brace to the json string
        return json ## Returns the json string
 
    def returnJsonString(self):
        print(self.create_json_string()) ## Prints to the JSON to Console
     
    def write_json_file(self): ## Writes the JSON string to a file
        try: ## Exception handling
            with open(self.output_fileName, "w") as f:
              f.write(self.create_json_string()) ## Writes the JSON string to the file using the returned function
        except:
            print(f"\n{self.output_fileName} not found") ## If the file is not found
        else:
            print(f"\nOutput Written to {self.output_fileName}") ## Confirm the completion of writing the file

       
if __name__ == "__main__":
    ## Creates instance of class
    project7 = CSVtoJSON()
    
    ## Reads the Txt Filet
    project7.read_txt_file()
    # print(project7.read_filename) ## Checks to see if the file was read
   
    ## Assigns the header of the txt file
    project7.assign_header()
    # print(project7.header) ## Checks to see if the header was assigned

    ## Pairs the header with the values of the txt file
    project7.pair_header_values()
    # print(project7.data) ## Checks to see if the data was written to the data variable
 
    ## Creates the JSON strings
    project7.create_json_string()
    # print(project7.create_json_string())

    ## Returns the JSON string to the screen
    project7.returnJsonString()
    ## THis will return to the console the JSON string

    ## Returns the JSON string to the file
    project7.write_json_file()
    ## This will write the JSON string to a file

