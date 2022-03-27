import colorgram
import turtle
from random import choice

# Initializes turtle object
t = turtle.Turtle()
turtle.colormode(255)
t.penup()

# Initialize image colors
img = colorgram.extract('hirst-example.jpg', 16)
color_options = []

# Used to obtain the RGB codes
def getColors():
    for color in img:
        color_options.append(((color.rgb.r), (color.rgb.g), (color.rgb.b)))
    i = len(color_options) - 1
    while i >= 0:
        c1, c2, c3 = color_options[i]
        if 235 < c1 < 255:
            del color_options[i]
        i-=1


# Implements drawing
getColors()
print(color_options)
for y in range(-250, 250, 50):
    for x in range(-250, 250, 50):
        t.goto(x,y)
        t.dot(20, choice(color_options))


# Initiates Screen object
screen = turtle.Screen()
screen.exitonclick()

