## Shrinking Guest list
## You just found out that your new dinner table won’t 
## arrive in time for the dinner, and you have space for only two guests

## Dinner List
dinnerList = ['Michael Jackson','Allah','Jesus']

## New bigger table print message
print("We have found a bigger Table!")
print("We will have more guests !!\n\n")

## Add at the end of the list
dinnerList.append('Drake')

## Add at the Beginning of the List
## .insert Format is 'index Position' -> 'Item'
dinnerList.insert(0, 'Beyonce')

## Add at the middle of the list
dinnerList.insert(3, 'Tyga')

## Checking what list looks like
print(f"{dinnerList}\n\n")

## Print New Invitation Messages
print(f"This is a formal invitation to: {dinnerList[0]}")
print(f"This is a formal invitation to: {dinnerList[1]}")
print(f"This is a formal invitation to: {dinnerList[2]}")
print(f"This is a formal invitation to: {dinnerList[3]}")
print(f"This is a formal invitation to: {dinnerList[4]}")
print(f"This is a formal invitation to: {dinnerList[5]}")
print('Come to dinner.\n\n')

## Line that prints only 2 people
print("Only allowed to bring 2 people now ?!\n")

## Dinner list Before pop
print(dinnerList)

## .pop assigned it to a variable so i can print out the message apologizing
newDinnerList = dinnerList.pop()
print(f"\n\nSorry {newDinnerList} but you cant come to dinner")
newDinnerList = dinnerList.pop()
print(f"Sorry {newDinnerList} but you cant come to dinner")
newDinnerList = dinnerList.pop()
print(f"Sorry {newDinnerList} but you cant come to dinner")
newDinnerList = dinnerList.pop()
print(f"Sorry {newDinnerList} but you cant come to dinner")

## Still in dinner list and still invited
print(f"\n\nSo great to still have: {dinnerList[0]} coming")
print(f"So great to still have: {dinnerList[1]} coming")
print(dinnerList)

print("\n Now deleting the list and checking.")
## Using Del to empty the list
## Using index 0 because list is basically empty
## format is del listname[indexposition]
del dinnerList[0]
del dinnerList[0]

print(dinnerList)

