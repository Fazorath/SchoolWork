# ## Returning a simple Value using Functions
# def get_formatted_name(firstname,lastname):
#     fullname = f"{firstname} {lastname}"
#     return fullname.title()

# musician = get_formatted_name("Yoenis","The goat")
# print(musician)

## Making an argument Optioanl
# def get_formatted_name(firstname,lastname,middlename=""):
#     if middlename:
#         fullname = f"{firstname} {middlename} {lastname}"
#     else:
#         fullname = f"{firstname} {lastname}"
#     return fullname.title()

# goat = get_formatted_name("yoenis","Hernandez")
# goatwithmiddlename = get_formatted_name("yoenis","Hernandez","Luis")
# print(goat)
# print(goatwithmiddlename)

## Returning a dictionary
# def buildPerson(fistname,lastname,age=None):
#     person = {'first':fistname, 
#                'last':lastname}
#     if age:
#         person['age'] = age
#     return person

# god = buildPerson("Yoenis","Hernandez", 24)
# print(god)


## using a function with a while loop
# def getformattedname(firstname,lastname):
#     fullname = f"{firstname.title()} {lastname.title()}"
#     return fullname

# while True:
#     print("\nPlease tell me your name:")
#     print("Enter q at any time")
#     fname = input("First Name: ")
#     if fname == 'q':
#         print("Program quit parameter met")
#         break
#     lname = input("Last Name: ")
#     if lname == 'q':
#         print("Program quit parameter met")
#         break
#     formattedname = getformattedname(fname,lname)
#     print(f"Hello, {formattedname}")


# ## Passing a list
# def greet_user(names):
#     for name in names:
#         msg = f"Hello, {name.title()}, this is a test of using dictionaries and loops"
#         print(msg)

# names = ['yoenis','yannah']
# greet_user(names)


## Modifyin a list in a function
# unprinted = ['phone','robot','pendant']
# completed = []

# Simulate printing design
# Move design from unprinted to completed models after printing
# def printmodels(unprinted,completed):
#     print("Need to Complete:")
#     while unprinted:
#         currentdesign = unprinted.pop() # Will start with Pendant
#         print(f"Printing model: {currentdesign}")
#         completed.append(currentdesign)

# # Display completed Models
# def completedmodels(completed):
#     print(f"\nThe following models are completed:")
#     for model in completed:
#         print(model)
# # split the
# printmodels(unprinted,completed)
# completedmodels(completed)


## Arbitrary Number of Arguments
# def makePizza(*toppings):
#     print("Today we are making a pizza with these ingredients:")
#     for topping in toppings:
#         print(f"- {topping}")

# # makePizza("By adding * infront of our parameter arg \nwe are able to provide as many as we want",'\narg2 just to show','\narg3 aswell')
# makePizza("pepper",'eggs','bacon','frits')

## Mixing positional and arbitrary arguments
# def makePizza(size,*toppings):
#     print(f"Making a {size}-inch pizza with these toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# makePizza(55,"bacon","eggs") # Assigns first value to positial and the rest to arbitrary

## Arbitrary Keyword Arguments
def buildPerson(first,last,**userinfo): ## ** makes python create an empty dictionary
    userinfo['first_name'] = first
    userinfo['last_name'] = last
    return userinfo

userprofile = buildPerson('Albert','Einstien',location='princeton',badbitches=45)
print(userprofile)
