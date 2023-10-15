## Fill in the blanks to have the function below to multiply the values up through num (i.e. 1*2*3...*num) 
# and return the result.  The result printed should be the values through the number 8.

## def compareDiceEqual(secondDie,firstDie):
   ## if(firstDie>secondDie):
   ##     print("First is greater than the second")
   ## elif(firstDie<secondDie):
   ##     print("Second is greater than the First")
   ## elif(firstDie==secondDie):
   ##     print("Dice are equal")

## compareDiceEqual(1,2)
def addValues(number):
    sum = 0
    currentNum = 1
    while(currentNum <= number ):
        sum+= currentNum
        currentNum+=1
    return sum

def main():
    print(addValues(5))

main()
