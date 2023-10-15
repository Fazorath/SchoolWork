# countries = ['Palestine', 'germany', 'France', 'brazi', 'Bali'] #List of Countries

# for country in countries: # For Loop creates a variable
#   print(f"I would love to visit: {country.title()}") # <-For every country print 

# print("\nThat is Every County in the world.") ## Statement at the end of the Foor Loop

## Creating Numbers
# for value in range(1,6): ## Numerical Lists
#   print(value) ## Off by one behavior like in Lists

## Making a list of Numbers by Converting range into List
# NumberOfYannahLs = list(range(1,16)) # Using list transforms it into a list
# print(f"A list of the number of Ls Yannah has taken:\n {NumberOfYannahLs}\n")

# ## Printing Minimum Number
# print(min(NumberOfYannahLs))

# ## Printing Maximum Number
# print(max(NumberOfYannahLs))

# ## Printin Sum of Number
# print(sum(NumberOfYannahLs))

## List Comprehension
# squares = [value**2 for value in range(1,11)]
# print(squares)

## Slicing A list
Animal_with_char = ['Bear','Beaver','Zebra','Lions','Meerkat']
# print(Animal_with_char[0:2]) ## index but with colon to choose which ones to work with.
# for animal in Animal_with_char[0:3]:
#   print(f"\nAnimal: {animal}")

## Copying a list using Slices
# animals = Animal_with_char[:] ## Empty Brackets
# animals.insert(0, 'Yannah') 
# print(f"\n{animals}")
# print("\nProve 2 Different Lists")
# print(f"\n{Animal_with_char}")

# ## A tuple 
# dimensions = (200, 50) ## defined with Parenthesis

# print("\nOriginal Tuple")
# for dimension in dimensions: ## For loop in Tuples
#   print(dimension)

# print("\nModified Tuple")
# dimensions = (400, 50) ## Reassigned the variables rather than changing
# for dimension in dimensions: ## For loop in Tuples
#   print(dimension)
