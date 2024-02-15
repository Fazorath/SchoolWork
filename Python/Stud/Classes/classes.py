class Dog:  # Define a class called dog / Capital represents a class
    '''A simple attempt at modeling a dog'''

    def __init__(self, name, age):
        '''Initialize name and age attributes'''
        self.name = name
        self.age = age

    def sit(self):
        '''Simulate the dog sitting in response to a command'''
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        '''Simulate rolling over in response to a command'''
        print(f"{self.name} rolled over!")

Dog1 = Dog('Willie', 6) # Create an instance of a class 
Dog2 = Dog('Lucy', 3) # Create an instance of a class


print(f"My dog's name is {Dog1.name}.") # Accessing attributes
print(f"My dog is {Dog1.age} years old.") # Accessing attributes
Dog1.sit() # Calling methods    
print("\n")
print(f"My dog's name is {Dog2.name}.") # Accessing attributes
print(f"My dog is {Dog2.age} years old.") # Accessing attributes
Dog2.sit() # Calling methods
