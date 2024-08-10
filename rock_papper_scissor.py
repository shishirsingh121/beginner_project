import random

option=["rock","paper","scissors"]
while True:
    user_input=input("enter the rock paper scissor:").lower()
    if user_input=="q":
        quit()
    if user_input not in option:
        continue
    random_number=random.randint(0,2)  
    computer_pick=option[random_number]
    print("computer choose: "+ computer_pick)
    if user_input=="rock" and computer_pick=="scissors":
        print("you won")
    elif user_input=="paper" and computer_pick=="rock":
        print("you won")
    elif user_input=="scissors" and computer_pick=="paper":
        print("you won")
    else:
        print("computr won") 
        break
print("good bye")           