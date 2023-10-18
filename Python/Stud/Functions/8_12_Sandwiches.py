def sandwiches(bread,*toppings):
    print("Summary of sandwich being ordered")
    print(f"The bread is {bread}")
    for topping in toppings:
        print(f"- {topping}")

# sandwiches('white','Hello6','Hello5','Hello4','Hello3','Hello2')
sandwiches('white','Hello6','Hello5','Hello4','Hello3','Hello2')
bread = input("what type of bread would you like: ")
toppings = input("What topping would you like: ")

sandwiches(bread,toppings)
