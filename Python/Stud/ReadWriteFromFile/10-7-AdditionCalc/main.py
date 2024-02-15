## While loop on 10-6
while True:
  try:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))

  except ValueError:
    print("wrong thing dumbass")
  else:
    print(number1 + number2)