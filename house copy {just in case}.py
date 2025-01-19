from turtle import *


speed('fastest')

penup()

goto(-200, -200)
pendown()

color('hotPink')
begin_fill()

for i in range(4):
    forward(500)
    left(90)
    forward(300)
    left(90)
end_fill()

forward(200)


color('SlateBlue2')
begin_fill()


for i in range(2):
    forward(100)
    left(90)
    forward(200)
    left(90)
end_fill()
 
penup()
backward(200)
left(90)
forward(130)
right(90)
forward(50)
pendown()
# go to circle start i window start pos
penup()
forward(50)
pendown()



#---------------------------window start---------------------------
#window top circle
color(166/255, 227/255, 255/255)
begin_fill()
circle(70)
end_fill()

penup()
backward(70)
pendown()

# window pink mask
color('hotpink')
begin_fill()
for i in range(2):
    forward(140)
    left(90)
    forward(80)
    left(90)
end_fill()


penup()
forward(20)
pendown()

# window yellow part
color('yellow')
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(80)
    left(90)
end_fill()
#---------------------window end-------------------------------------------



#--------------------------- making second window ---------------------------

penup()
forward(350)
pendown()


#---------------------------window start---------------------------
#window top circle
color(166/255, 227/255, 255/255)
begin_fill()
circle(70)
end_fill()

penup()
backward(70)
pendown()

# window pink mask
color('hotpink')
begin_fill()
for i in range(2):
    forward(140)
    left(90)
    forward(80)
    left(90)
end_fill()


penup()
forward(20)
pendown()

# window yellow part
color('yellow')
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(80)
    left(90)
end_fill()
#---------------------window end-------------------------------------------

penup()
forward(50)
left(90)
forward(170)
pendown()

print(pos())   # (200.00,105.00)

penup()
color(1/255, 147/255, 192/255)
begin_fill()
forward(150)
left(90)
forward(300)
left(90)
forward(150)
left(90)
forward(300)
end_fill()

#------------------second part of roof--------------------------------------------------------


backward(140)
color(23/255, 190/255, 242/255)
begin_fill()
forward(300)
left(135)
forward(250)
left(100)
forward(210)
end_fill()

right(54.1)
penup()
forward(20)
pendown()


color(23/255, 190/255, 242/255)
begin_fill()
forward(300)


right(135)
forward(250)
right(100)
forward(215)
end_fill()

#----------------------------------

color(255/255, 87/255, 110/255)
penup()
left(54.1)
forward(20)
forward(290)
left(135)
forward(245)
left(105)
forward(30)
right(54.1)
forward(35)
pendown()




##chimney-----------------


begin_fill()
right(95)
forward(30)
right(90)
forward(10)
left(90)
forward(25)
left(90)
forward(40)
left(90)
forward(25)
left(90)
forward(10)
right(90)
forward(30)
end_fill()

#------------mailbox----------------


penup()
home()

goto(-200, -200)




bk(100)
right(90)
fd(80)
pendown()

color(90/255, 76/255, 76/255)
begin_fill()

forward(65)
right(90)
forward(15)
right(90)
fd(65)

left(90)
forward(15)
#circle(-15, 70)

right(90)
forward(8)
right(90)
forward(45)
right(90)
forward(8)
right(90)
forward(15)
##forward(5)
##
##left(100)
##forward(45)
end_fill()

left(90)
forward(65)
right(90)
forward(15)
right(90)
fd(65)
left(90)
fd(15)
right(90)
forward(8)
right(90)
forward(8)




color(205/255, 150/255, 150/255)
begin_fill()
left(100)
forward(50)
right(75)
forward(25)
right(55)
forward(25)
right(65)
fd(48.5)
end_fill()

color('black')
penup()
right(90)
forward(16)
right(110)
forward(20)
pendown()

begin_fill()
circle(10)
print(pos())
end_fill()
#--------------------------roof of mailbox--------------
color(90/255, 76/255, 76/255)

penup()

fd(30)
right(90)

pendown()

begin_fill()
fd(5)
left(90)
forward(5)
left(85)
forward(33)
left(54)
forward(33)
left(90)
fd(7)
left(95)
fd(32)

right(65)
forward(33)

end_fill()



penup()

goto(-298.09,-253.49) 


color(166/255, 107/255, 107/255)
right(90)
fd(13)
right(50)
pendown()
begin_fill()

fd(10)

left(90)



fd(3)
left(90)
fd(15)
left(90)
fd(3)
left(90)
forward(5)

end_fill()

penup()
right(80)
fd(300)
right(5)
pendown()
color(246/255, 149/255, 83/255)
begin_fill()
right(10)
for i in range(4):
    forward(100)
    left(90)
end_fill()
    
penup()    
left(90)
forward(50)
pendown()

color(249/255, 224/255, 127/255)
begin_fill()
circle(-50)
end_fill()


penup()
circle(-50, 45)

fd(50)
pendown()

color(255/255, 175/255, 122/255)
begin_fill()
for i in range(4):
    right(90)
    fd(100)
end_fill()


color(249/255, 224/255, 127/255)

right(90)
forward(50)
begin_fill()
circle(-50)
end_fill()

penup()

goto(-200, -200)
pendown()
left(45)

color(116/255, 240/255, 153/255)
begin_fill()

circle(-60, 180)
end_fill()
penup()
left(90)

bk(90)
left(90)
pendown()
color(167/255, 251/255, 192/255)
begin_fill()
circle(30, 180)
end_fill()
left(91)
penup()
goto(-200, -200)
fd(500)















































































































