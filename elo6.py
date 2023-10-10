import turtle
import random
s = turtle.Turtle()
colors = ('violet' , 'blue' , 'green', 'red')

for i in range(12):
    for u in range(2):
        s.color(random.choice(colors))
        s.forward(60)
        s.right(30)
        s.forward(60)
        s.right(150)
    s.right(30)