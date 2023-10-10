import turtle
ldr = turtle.Turtle

def forma():
    for _ in range(6):
        ldr.forward(30)
        ldr.right(60)

def jump(s):
    ldr.up()
    ldr.forward(s)
    ldr.down()

for _ in range(6):
    for _ in range (2):
        for _ in range(4):
            forma()
            jump(75)
        jump(-25)
        ldr.rigth(60)
        jump(25)
        ldr.right(120)
    jump(-25)
    jump(50)
    ldr.right(60)