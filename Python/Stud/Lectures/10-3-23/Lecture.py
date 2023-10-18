## Defining 2 Functions

## Functioning calling another function
def makepizza():
    sauce = getIngredient()
    dough = getIngredient()
    topping = getIngredient()
    topping2 = getIngredient()
    print("\n",sauce)
    print("\n",dough)
    print("\n",topping)
    print("\n",topping2,'\n')

def getIngredient():
    ingredient = input("\nWhat is the Ingredientsss: ")
    return ingredient

def getIngredientError():
    ingredient = input("What is the Ingredient: ")
    ingredient2 = input("What is the Ingredient: ")
    ingredient3 = input("What is the Ingredient: ")
    return ingredient ## Returning one element that is a list using []

print(getIngredientError())

makepizza() # Runs the entire code
