from turtle import *
import random
speed(0)

for i in range(200): 
    angle = random.randint(10, 350) 

    color(random.random(), random.random(), random.random())
    begin_fill()
    fd(100)
    left(angle)
    fd(100)
    left(180 - angle)
    fd(100)
    left(angle)
    fd(100)
    end_fill()



    penup()
    goto(random.randint(-400, 500),random.randint(-400, 500))

    angle = random.randint(10, 350) 

    color(random.random(), random.random(), random.random())
    begin_fill()
    fd(100)
    left(angle)
    fd(100)
    left(180 - angle)
    fd(100)
    left(angle)
    fd(100)
    end_fill()




























