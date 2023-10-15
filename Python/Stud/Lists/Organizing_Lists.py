## Using .sort
dinnerList = ['Michael Jackson','Allah','Jesus']

## Using sort will organize list Alphabetical
dinnerList.sort()
print("Sorted Alphabetically\n")
print(dinnerList)

## Using the Arg reverse=true will reverse the order making it backwards
dinnerList.sort(reverse=True)
print(dinnerList)

## Sorted will not affect the actual list
## Format is sorted(item)
print(sorted(dinnerList))
print(dinnerList)

## Printing a list in reverse using .reverse
## Not alphabetical just reversed
dinnerList.reverse()
print(dinnerList)

## Finding the Lenght using len
## Format is len(item)
len(dinnerList)
print(len(dinnerList))
