import random
#Task 3
#Guess the Number --->
number = random.randint(1 , 50)#helps to select a random number
#print(number)
attempts=0

print("Guess the number between 1 to 50")

while True:
    guess = input(input("Enter your Guess : "))
    attempts+=1
    if guess>number:
        print("Guess to High")
    elif guess<number:
        print("Guess to low")
    else:
        print("Congrats, You found the correct number")
        break



