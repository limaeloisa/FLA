from turtle import *

e = Turtle()

e.shape('turtle')
#desenhando o tabuleiro com turtle
e.pensize(2)
e.speed(10)
e.forward(200)
e.backward(300)
e.left(90)
e.penup()
e.forward(100)
e.pendown()
e.right(90)
e.forward(300)
e.backward(100)
e.left(90)
e.forward(100)
e.backward(300)
e.forward(100)
e.right(90)
e.backward(100)
e.left(90)
e.forward(200)
e.backward(300)


#função de centralização do xis
#recebe as coordenadas  e move a turtle para o centro do quadrante
def cent(x, y):
    e.penup()
    e.goto(x - (x % 100) + 50, y - (y % 100) + 50) 
    e.pendown()

#função desenhando o xis
def xis():
   e.pencolor('violet')
   e.right(45)
   e.forward(50)
   e.backward(100)
   e.forward(50)
   e.left(90)
   e.forward(50)
   e.backward(100)
   e.right(45)

# função desenhando a bolinha
def ball():
     e.color('blue')
     e.pensize(2)
     e.speed()
     e.penup()
     e.forward(45)
     e.left(90)
     e.pendown()
     e.circle(45)
    

#comandos de interação
onscreenclick(cent) #centralizando com o click
onkey(xis, 'space')
listen() #escuta os eventos de teclado
onkey(ball, 'c') #realiza os eventos
listen()
mainloop()