def goingthroughlist(listOb):
    print(listOb) ## List Before pop
    while listOb: ## Keeps going through list as long as it has an element inside 
        print(listOb.pop())
    print("\nList is now Empty:")
    print(listOb) ## List After Modified by Pop

names = ['Yoenis','Yannah','Brandon']
goingthroughlist(names)

def throughlist2(listOb):
    print(listOb) ## List Before pop
    listcopy = listOb[:] ## Copy of Original List
    listcopy.sort() #Another way of sorting
    
    while listcopy: ## Now going through the list copy
        # listcopy.reverse() # Reversing through the list
        print(listcopy.pop())
    print("\nList is now Empty:")
    print(listcopy) ## List Copy is now empty
    print(listOb) ## Original List is still intact

names = ['Yoenis','Yannah','Brandon']
goingthroughlist(names)
