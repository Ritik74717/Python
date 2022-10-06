import random
num = random.randint(1,100)
#print(num)
guesses=0
userguess=None

while(userguess!=num):
    userguess = int(input("Enter a number\n"))
    guesses=guesses+1
    if(userguess==num):
        print("You guess Correct!")
    elif(userguess>num):
        print("You Guessed Wrong Please Enter Smaller Number")
    else:
        print("You Guessed Wrong Please Enter Greater Number")

print(f"Your guessed in {guesses}")
