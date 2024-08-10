print("welcome to my computer quiz?")
playing=input("do you want to play: ")
if playing.lower() != "yes":
    quit()
print("okey! lets play..")
score=0
answer=input("what does cpu stand for?")
if answer.lower()=="central processing unit":
    print("right answer.")
    score+=1
else:
    print("you have an incorrect answer, sorry!")    
answer=input("what does gpu stand for?")
if answer.lower()=="graphic processing unit":
    print("right answer.")
    score+=1
else:
    print("you have an incorrect answer, sorry!") 
answer=input("what does mu stand for?")    
if answer.lower()=="memory unit":
    print("right answer.")
    score+=1
else:
    print("you have an incorrect answer, sorry!")   

print(f"the total right answer is {score}") 
print(f"the total percentage is {score*100/3}%")     