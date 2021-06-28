print("author: NacreousDawn596")
print("github: https://github.com/NacreousDawn596")

import turtle
from turtle import *
def buttonclick(x,y):
	print("{0}, {1}".format(x, y))
onscreenclick(buttonclick,1)
speed(1)
hideturtle()
color('red')
pensize(3)
left(48)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
penup()
goto(-4, -71)
pendown()
write("I love you", align='center', font=('arial black', 20, 'normal'))
done()
