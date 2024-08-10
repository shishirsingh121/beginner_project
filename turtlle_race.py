import turtle
import random
import time
WIDTH,HEIGHT=500,500
COLORS=['red','green','blue','gray','yellow','black','pink','voilet','dark blue']

def numbers_of_racers():
    racers=0
    while True:
        racers=input("enter the number of racers from 1 to 10: ")
        if racers.isdigit():
            racers=int(racers)
        else:
            print("enter the valid number...")
            continue
        if 2<=racers<=10:
            return racers
        else:
            print("you only allow to 2 to 10 racers")
def create_turtle(color):
    turtle=[]
    for i,color in enumerate(color):#enumurate give value and index of all element
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        
        
    

def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('turtle racing')
obj=numbers_of_racers()  
init_turtle()  
random.shuffle(COLORS)
color=COLORS[:racer]

