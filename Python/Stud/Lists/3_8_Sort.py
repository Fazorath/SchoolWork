## Seeing the Word
## Think of atleast five palces in the world you would like to visit

## List of Locations
places = ['Bali','Germany','Brazi','France','Palestine']
print(places) # Printing Raw

## Printing my list sorted in alphabetical but without
## Changing the Actual list using sorted
print(sorted(places))
print(places) # List still in Original Order

## Sorted but in Reverse
## Format is Sorted(Item, Arg)
print(sorted(places, reverse=True))
print(places) #List still in Original Order

## Using .reverse() to change the order
places.reverse() #Reversed
print(places) #Original List Has been Altered
places.reverse() #Reversed 

## Using .sort() to sort in alphabetical Order
places.sort()
print(places)

## Sort again but using the reverse=true Arg
places.sort(reverse=True)
print(places)
