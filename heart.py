from turtle import *


hideturtle()

title("Love Heart ❤️❤️")



pensize(8)

def heart():

    color('red')
    begin_fill()

    left(45)
    forward(110)
    circle(45,225)

    right(180)
    circle(45,225)
    forward(108)
    left(90)

    end_fill()
    
 
def b1():

    # pensize(5)
    color('blue')

    seth(90)
    forward(20)
    left(90)
    forward(20)

    # penup()
    # setposition(-100,-40)
    # pendown()
    # seth(90)
    # forward(20)
    # left(90)
    # forward(20)

    # penup()
    # setposition(-90,-30)
    # pendown()
    # seth(90)
    # forward(20)
    # left(90)
    # forward(20)


 
heart()   



x = -110
y = -50

penup()
setposition(x,y)
pendown()


for i in range (3):
    
    b1()
    penup()
    x = x + 10
    y = y + 10
    setposition(x,y)
    pendown()



penup()
setposition(-110,-30)
seth(0)
pendown()
left(45)
forward(160)

penup()
setposition(67.7696,147.7696)
pendown()
seth(0)
pendown()
left(45)
forward(90)

penup()
setposition(131.4092,191.4092)
pendown()
b1()


mainloop()