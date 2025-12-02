from turtle import *

speed(10)

bgcolor('black')
hideturtle()

pensize(5)

penup()
# setposition(-440, -120)
setposition(-440, -70)
pendown()



def base():
    begin_fill()
    color('brown')
    right(100)
    forward(170)
    # forward(150)
    left(60)
    circle(100, 80)
    left(60)
    forward(170)
    # forward(150)
    left(80)
    end_fill()
    # forward(75)

def right_top1():
    # color('green')
    left(120)
    circle(300, 60)
    left(130)
    forward(250)

def right_top2():
    # left(120)
    circle(200, 60)
    left(120)
    forward(150)

def right_top3():
    circle(200, 50)
    left(120)
    forward(252)



def left_top3():
    forward(252)
    left(120)
    circle(200, 50)

def left_top2():
    forward(150)
    left(120)
    circle(200, 60)

def left_top1():
    # left(120)
    forward(250)
    left(130)
    circle(300, 60)

def star():
    color('yellow')
    begin_fill()
    left(37)
    forward(77)
    seth(180)
    forward(133)
    seth(270)
    left(57)
    forward(133)
    seth(90)
    left(20)
    forward(133)
    seth(180)
    left(72)
    forward(133)
    seth(0)
    left(32)
    forward(56)
    end_fill()


def balls():
    begin_fill()
    color('red')
    circle(10,360)
    end_fill()


def M():
   
    pencolor('red')
    forward(100)
    seth(270)
    left(45)
    forward(60)
    seth(0)
    left(45)
    forward(60)
    seth(0)
    right(90)
    forward(100)
    penup()
    

def E():
    pencolor('blue')
    forward(100)
    right(90)
    forward(70)
    penup()
    setposition(70, 200)
    seth(0)
    pendown()
    forward(50)
    penup()
    setposition(70, 150)
    seth(0)
    pendown()
    forward(70)
    penup()
    

def R():
    pencolor('green')
    forward(100)
    left(90)
    circle(25, -180)
    seth(270)
    left(45)
    forward(70)
    penup()

def Y():
    pencolor('orange')
    forward(50)
    left(45)
    forward(70)
    penup()
    setposition(350, 200)
    seth(0)
    pendown()
    left(45)
    forward(70)
    penup()


def C():
    pencolor('yellow')
    right(10)
    circle(50, 200)
    penup()


def H():
    pencolor('orange')
    forward(100)
    penup()
    setposition(-40, 70)
    seth(0)
    pendown()
    forward(50)
    left(90)
    forward(50)
    seth(270)
    forward(100)
    penup()

def I():
    pencolor('aqua')
    forward(100)
    left(90)
    forward(30)
    seth(0)
    forward(60)
    penup()
    setposition(160, 20)
    seth(180)
    pendown()
    forward(30)
    seth(0)
    forward(60)
    penup()


def S():
    pencolor('#12b9b1')
    seth(180)
    right(30)
    circle(26, 220)
    seth(180)
    right(20)
    circle(26, -220)
    penup()


def T():
    pencolor('yellow')
    forward(100)
    left(90)
    forward(35)
    seth(0)
    forward(70)
    penup()

def A():
    pencolor('white')
    right(20)
    forward(110)
    seth(0)
    right(70)
    forward(110)
    penup()
    setposition(530, 70)
    seth(0)
    pendown()
    forward(32)
    penup()






base()
penup()

setposition(-400,-70)
pendown()
color('#00932c', '#4cff2c')

begin_fill()

right_top1()
penup()

setposition(-400, 30)
right(175)
pendown()

right_top2()
penup()

setposition(-400, 130)
right(175)
pendown()

right_top3()
seth(180)
left(50)

left_top3()
penup()

setposition(-484, 85)
right(175)
pendown()

left_top2()
penup()

setposition(-500, -23)
right(175)
pendown()

left_top1()
end_fill()
penup()

setposition(-400, 287)
seth(0)
pendown()


star()
penup()
setposition(-397, -68)
pendown()

balls()
penup()
setposition(-397, 30)
pendown()

balls()
penup()
setposition(-397, 127)
pendown()

balls()
penup()
setposition(-397, 260)
pendown()

balls()
penup()
setposition(-600, -190)
pendown()

balls()
penup()
setposition(-515, -110)
pendown()

balls()
penup()
setposition(-290, -100)
pendown()

balls()
penup()
setposition(-190, -200)
pendown()

balls()
penup()
setposition(-540, -15)
pendown()

balls()
penup()
setposition(-470, 30)
pendown()

balls()
penup()
setposition(-320, 30)
pendown()

balls()
penup()
setposition(-250, -15)
pendown()

balls()
penup()
setposition(-490, 110)
pendown()

balls()
penup()
setposition(-400, 190)
pendown()

balls()
penup()
setposition(-300, 110)
pendown()

balls()
penup()


pensize(10)

setposition(-50, 150)
seth(90)
pendown()
M()

setposition(70, 150)
seth(90)
pendown()
E()

setposition(180, 150)
seth(90)
pendown()
R()

setposition(260, 150)
seth(90)
pendown()
R()

setposition(350, 150)
seth(90)
pendown()
Y()


setposition(-80, 120)
seth(180)
pendown()
C()

setposition(-40, 20)
seth(90)
pendown()
H()

setposition(50, 20)
seth(90)
pendown()
R()

setposition(160, 20)
seth(90)
pendown()
I()

setposition(260, 120)
seth(90)
pendown()
S()

setposition(330, 20)
seth(90)
pendown()
T()

setposition(400, 20)
seth(90)
pendown()
M()

setposition(510, 20)
seth(90)
pendown()
A()

setposition(640, 120)
seth(90)
pendown()
S()











mainloop()