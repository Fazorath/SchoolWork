## 3.5 Chaning Guest list
## You just heard that one of your guests can’t make the 
## dinner, so you need to send out a new set of invitations. You’ll have to think of 
## someone else to invite


## Dinner List
dinnerList = ['Michael Jackson','Allah','Jesus']

## Print Messages
print(f"This is a formal invitation to: {dinnerList[0]}")
print(f"This is a formal invitation to: {dinnerList[1]}")
print(f"This is a formal invitation to: {dinnerList[2]}")
print('Come to dinner.')

## Guest who cant make it
print(f"Guests Who cant Attend: {dinnerList[1]}\n\n")

## New Guest
dinnerList[1] = 'Drake'

#Print Messages After New Guest
print("New Dinner List:")
print(f"This is a formal invitation to: {dinnerList[0]}")
print(f"This is a formal invitation to: {dinnerList[1]}")
print(f"This is a formal invitation to: {dinnerList[2]}")
print('Come to dinner.\n\n')
