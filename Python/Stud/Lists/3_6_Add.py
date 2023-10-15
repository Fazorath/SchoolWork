## 3.6 More Guests
##  You just found a bigger dinner table, so now more space is 
## available. Think of three more guests to invite to dinner.

## Dinner List
dinnerList = ['Michael Jackson','Allah','Jesus']

## Print Messages
# print(f"This is a formal invitation to: {dinnerList[0]}")
# print(f"This is a formal invitation to: {dinnerList[1]}")
# print(f"This is a formal invitation to: {dinnerList[2]}")
# print('Come to dinner.\n\n')

## New bigger table print message
print("We have found a bigger Table!")
print("We will have more guests !!\n\n")

## .insert Format is 'index Position' -> 'Item'
dinnerList.append('Drake') ## Add at the end of the list
dinnerList.insert(0, 'Beyonce') ## Add at the Beginning of the List
dinnerList.insert(3, 'Tyga') ## Add at the middle of the list

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


