from turtle import *

width(7)
speed(4)

color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
left(90)
color("green")
begin_fill()
forward(120) 
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("yellow")
begin_fill()
right(120)
forward(118)
left(60)
forward(118)
end_fill()


penup()
color("blue")
begin_fill()
goto(58,120)
pendown()
right(30)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)
end_fill()

penup()
color("blue")
begin_fill()
goto(146,120)
pendown()
right(-90)
forward(50)

right(-90)
forward(50)

right(-90)
forward(50)

right(-90)
forward(50)
end_fill()

exitonclick()
