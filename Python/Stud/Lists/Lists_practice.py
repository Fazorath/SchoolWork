## Wed Oct 11, 2023


Planets = ['Pluto','Mars','Earth','Jupiter','Uranus']

print(len(Planets)) #Print the amount of Items in the list

print(f"These are the planets Using Sorted: {sorted(Planets)}\n\n") 

print("Add to the front using .insert(position, item):")
Planets.insert(0, 'Your Mother')
print(f"{Planets}\n")

print("Removes the last item in the list using .pop(): ")
print(Planets)
popped = Planets.pop()
print(Planets)
print(f"Popped item was the last: {popped}")

print("\n'Mars' Was changed using index position: ")
Planets[2] = 'Egg'
print(f"{Planets}")

print("\nAdded 'end' at last index of the list using .append('Text'): ")
Planets.append('End')
print(Planets)

print("\nUsing .sort(arg) passing it reverse=True to reverse the order of the list Permanently: ")
Planets.sort(reverse=True)
print(Planets)
print("Passing same Argument Again with =False: ")
Planets.sort(reverse=False)
print(Planets)
