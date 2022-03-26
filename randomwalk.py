import random
from turtle import Turtle, Screen
import turtle
from random import choice

t = Turtle()
turtle.colormode(255)
dir = [90, 180, 270, 360]
t.speed("fastest")
t.width(10)
t.shape("circle")
i=0

def rnd_clr():
    r=random.randint(0, 255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return r,g,b

while i<301:
    t.color(rnd_clr())
    t.forward(15)
    t.right(choice(dir))
    i+=1


screen = Screen()
screen.exitonclick()