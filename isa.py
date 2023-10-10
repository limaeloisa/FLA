import turtle
import random
colors = ('violet','blue','green','red')
elo = turtle.Turtle()
def formas():
    for eb in range(6):
        elo.forward(25)
        elo.right(60)

for at in range(6):
    for me in range(2):
        elo.color(random.choice(colors))
        for u in range(4):
            formas
            elo.penup()
            elo.forward(75)
            elo.pendown()
        elo.penup()
        elo.backward(25)
        elo.left(60)
        elo.penup()
        elo.forward(50)
        elo.pendown()
        elo.right(60)