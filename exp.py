import random
min_val=3
max_val=23
opertors=['*',"+","-"]
total_problem=10
def expression():
   
    left=random.randint(min_val,max_val)
    right=random.randint(min_val,max_val)
    op=random.choice(opertors)
    exp=str(left)+" "+op+" "+str(right)
    answer=eval(exp)
    return exp,answer
correct=0
for i in range(total_problem):
    exp,answer=expression()
    correct=0
    while True:
        guess=input(f"problem no {str(i+1)}is expressionis {exp}")
        if guess==str(answer):
            break
             
        
            
        

        



