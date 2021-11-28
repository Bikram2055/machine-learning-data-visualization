import turtle
import math

s = turtle.getscreen()
t = turtle.Turtle()
a = turtle.Turtle()
turtle.title('drawing board')
turtle.bgcolor('red')

t.pensize(2)
t.fillcolor('yellow')
t.pencolor('green')
t.speed(10)

for i in range(10, 50):
    # t.pensize(2)
    # t.fillcolor('yellow')
    # t.pencolor('green')
    # t.speed(20)
    t.fd(i)
    t.lt(90)
    t.fd(i)
# t.goto(-100, 100)
# t.circle(50)
# t.fd(200)
# t.circle(50)
# t.rt(90)
# t.fd(200)
# t.rt(90)
# t.circle(50)
# t.fd(200)
# t.circle(50)
# t.rt(90)
# t.fd(200)
# m, c = 0.5, 5
# t.goto(0,105)
# t.goto(0,0)
# t.goto(100,0)
# t.goto(0,0)
#
# for x in range(100):
#     y = 50*math.cos(0.1*x)
#     t.goto(x, y)

s.mainloop()
