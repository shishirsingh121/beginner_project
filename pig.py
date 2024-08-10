import random
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

while True:
    players=input("enter the number of palyers: ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("enter the players")
    else:
        print("please enter the valid number")
        continue
max_score=50
player_score=[0 for _ in range(players)]
while max(player_score)<max_score:
    for i in range(players):
        print(f"player {i+1} turn is started")
        print("your total score is :", player_score[i])
        current_value=0
        while True:
            players_roll=input("do you want to roll: press y to roll: ")
            if players_roll.lower()!="y":
                break
            value=roll()
            if value==1:
                print("you rooled has done")
            else:
                current_value+=value
                print("you rolled a: ",value)
            print("your score is: ",current_value)
                    
        player_score[i]+=current_value
        print("ypur total score is: ",player_score[i]) 
max_score=max(player_score)
wining_ind=  player_score.index(max_score)
print("player winning is ",wining_ind+1,"total score is",max_score)      