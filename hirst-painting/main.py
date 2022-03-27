import colorgram
import turtle
from random import choice

img = colorgram.extract('hirst-example.jpg', 16)
color_options = []

# Used to obtain the RGB codes now in color_options
def getColors():
    for color in img:
        color_options.append(((color.rgb.r), (color.rgb.g), (color.rgb.b)))
    i = len(color_options) - 1
    while i >= 0:
        c1, c2, c3 = color_options[i]
        if 235<c1<255:
            del color_options[i]

def drawHirst():
    for i in range(0,11):
        for j in range(0,11):
            t.dot(20, choice(color_options))
            t.penup()
            t.forward

t = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()
screen.exitonclick()

