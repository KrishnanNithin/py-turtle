from turtle import Turtle, Screen
from random import choice
turt = Turtle()
turt.shape("turtle")

colors = ["blue", "spring green", "dark orange", "violet", "salmon", "orange", "orchid", "medium turquoise"]

def drawshape(sides):
    for i in range(sides):
        turt.forward(80)
        turt.right(360/sides)


for i in range(3, 11):
    turt.color(choice(colors))
    drawshape(i)

screen = Screen()
screen.exitonclick()