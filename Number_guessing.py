from random import randint
Number=randint(1,100)
n=10

for i in range(n):
    Guess=int(input("Enter the number: "))
    if(Number==Guess):
        print("You won ")
        print(f"You guessed the number in: {i+1} chance and the number is: {Number}")
        break
    if i == n-1:
        print("Game Over! You lose!")
        print(f"The number was: {Number}")
    elif(Guess<Number):
        print("Try higher")
    elif(Guess>Number):
        print("Try lower")
    elif(i>=n):
        print("You lose")
    else:
        print("Enter a valid number")


