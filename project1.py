# guess the number
import random

target = random.randint(1,100)

while True:
    usernumber = int(input("guess the target :" ))
    if(usernumber == target):
        print("correct guess")
        break
    elif(usernumber < target):
        print("your number was to small .. guess again")
    elif(usernumber > target):
        print("your number was big...guess again")
    


print("game over")
