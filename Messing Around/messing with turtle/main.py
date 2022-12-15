import turtle as t
import random as r
import math as m

turtles = []
for i in range(10):
    turtles.append(t.Turtle())
    turtles[i].speed(0)
    turtles[i].hideturtle()


for i in range(100):
    for j in turtles:
        j.pensize(r.randint(1, 10))
        j.pencolor(r.random(), r.random(), r.random())
        j.begin_fill()
        for x in range(10, 20):
            j.forward(x)
            j.left(r.randint(0, 360))
        j.end_fill()
        j.fillcolor("black")


t.done()
print("Done")