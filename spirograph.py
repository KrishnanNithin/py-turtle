import turtle as t
import random

tur = t.Turtle()
t.colormode(255)
tur.speed("fastest")
def rnd_clr():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def spirograph():
    for i in range(180):
        tur.color(rnd_clr())
        tur.circle(120)
        tur.setheading(tur.heading() + 2)

spirograph()
Screen = t.Screen()
Screen.exitonclick()