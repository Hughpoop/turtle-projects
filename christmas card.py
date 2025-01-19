from turtle import *
import turtle
import random
import time
speed(0)
bgcolor(246/255, 85/255, 118/255)
tree=turtle.Turtle()
turtle.register_shape("b2g77D8.gif")
tree.shape("b2g77D8.gif")
tree.pu()
tree.goto(100,0)

###C:\Users\Lev Kung\AppData\Local\Programs\Python\Python37-32
hideturtle()
pu()
goto(-400, 0)
bk(300)
color('white')
write('MERRY', font=('ravie', 40, 'italic'))
right(90)
fd(100)
left(90)
write('christmas', font=('ravie', 40, 'italic'))
right(90)
fd(100)
right(90)

write('TO ALL OF YOU', font=('Times New Roman', 40, 'italic'))


#new pen


pen = turtle.Turtle()
pen.hideturtle()
pen.pu()
pen.goto(-400, 0)
pen.bk(300)
pen.right(90)
pen.fd(100)
pen.fd(100)
pen.left(90)
pen.color('white')
pen.fd(370)
pen.left(90)
pen.fd(50)
pen.left(50)
pen.bk(10)
pen.pd()
pen.pd()
pen.pu()
for i in range(5):
    pen.dot(7, 'white')
    pen.fd(7)

pen.bk(7)
pen.right(120)
pen.color('red')
pen.begin_fill()
pen.pd()
pen.fd(30)
pen.right(120)
pen.fd(30)
pen.right(120)
pen.fd(30)
pen.end_fill()
pen.bk(30)
for i in range(5):
    pen.dot(7, 'white')
    pen.fd(7)
pen.pu()
pen.bk(7)
pen.right(120)
pen.fd(30)
pen.right(90)
pen.color('white')
pen.begin_fill()
pen.circle(3)
pen.end_fill()
pen.pd()

snows = []
for i in range(20):
    sn = Turtle()
    sn.hideturtle()
    sn.speed(0)
    sn.pu()
    sn.goto(random.randint(-430, 530), random.randint(-400, 400))
##    sn.pd()
    sn.dot(random.randint(5, 20), 'white')
    snows.append(sn)

    
Hugh_colors = ['red', 'violet', 'orange', 'green', 'purple']
    
for i in range(100):
    for snow in snows:
        snow.right(90)
        snow.goto(random.randint(-430, 530), random.randint(-400, 400))
        snow.dot(7, 'white')
##    bgcolor(random.choice(Hugh_colors))
    bgcolor(random.random(), random.random(), random.random())

 
Hugh_colors = ['red', 'violet', 'orange', 'green', 'purple']

for i in range(100):
    bgcolor(random.choice(Hugh_colors))
    time.sleep(0.5)
































