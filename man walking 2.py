from turtle import *


speed(0)
penup()
goto(-200, -200)
pd()
color(30/255, 144/255, 255/255)
begin_fill()
##frame----------------------------------
for i in range(2):
    fd(800)
    left(90)
    fd(500)
    left(90)
    
end_fill()



##ground---------------------------------    
color(124/255, 252/255, 0)
begin_fill()
fd(800)
left(90)
fd(100)
left(90)
fd(800)
left(90)
fd(100)
end_fill()
##Man----------------:]--------------
color('black')
pu()
left(180)
fd(120)
right(90)
fd(100)
pd()
print(pos())
##@@@@man body------------------[]----

color(0, 0, 255/255)
begin_fill()
for i in range(2):
    fd(80)
    left(90)
    fd(150)
    left(90)

end_fill()


color('purple')

begin_fill()
fd(12)
right(120)
fd(80)
right(90)
fd(12)
right(90)
fd(80)
end_fill()


#----------shoe  
bk(80)
right(90)
color('black')
begin_fill()
for i in range(2):
    fd(40)
    right(90)
    fd(20)
    right(90)
end_fill()
pu()
goto(-100.00, -80.00)
left(30)
fd(80 - 12)
pd()


right(60)
color('purple')
begin_fill()
for i in range(2):
    fd(80)
    left(90)
    fd(12)
    left(90)
end_fill()

fd(80)

color('black')
begin_fill()
for i in range(2):
    fd(20)
    left(90)
    fd(40)
    left(90)
end_fill()
##-------pos to hand---------------

pu()
goto(-100.00, -80.00)
left(30)
left(30)
fd(80)
left(90)
fd(150 - 10)
pd()
color('red')
begin_fill()
fd(10)
right(120)
fd(60)
left(90)
fd(30)
right(90)
fd(10)
right(90)
fd(40)
right(90)
fd(60)
end_fill()

###arm2------------
pu()
goto(-100, -80)
left(30)
right(90)
fd(150 - 10)
pd()
fd(10)
begin_fill()
left(150)
fd(50)
left(90)
fd(30)
left(120)
right(30)
fd(10)
left(90)
fd(15)
right(90)
fd(50)
end_fill()









































    





