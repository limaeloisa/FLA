import turtle
import random
a= turtle.Turtle()
colors = ('violet','blue','green','red')
for u in range(6):
 for i in range(6):
        a.color(random.choice(colors))
        a.forward(100)
        a.right(60)
 a.right(60)