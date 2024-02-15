## Value error for Str instead of Number input
try:
  number1 = int(input("Enter a number: "))
  number2 = int(input("Enter another number: "))

except ValueError:
  print("wrong thing dumbass")
else:
  print(number1 + number2)