import random as ra
a=ra.randrange(0,10)
while True:
    guess=input("enter the number between 1 to 10: ")
    if guess.isdigit():
        guess=int(guess)
    else:
        print("please continue")
        continue
    
    if guess==a:
        print("you are right")        
        break
     
    else:
        print("sorry please try again2")