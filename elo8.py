import turtle
import random
colors = ('blue')

ldr = turtle.Turtle()


def flor():
    for i in range(6):
        ldr.color(random.choice(colors))
        for u in range(8):
            ldr.forward(20)
            ldr.right(30)
        ldr.right(60)
        

for up in range(3):
    flor()
    ldr.penup()
    ldr.right(120)
    ldr.forward(150)
    ldr.pendown()
