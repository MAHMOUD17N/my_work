import turtle
import time

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")

for size in range(30, 81, 2):
    t.clear()
    t.color("red")
    t.write("Love", align="center", font=("Arial", size, "bold"))
    time.sleep(0.05)

for size in range(80, 29, -2):
    t.clear()
    t.color("white")


    t.write("Love you", align="center", font=("Arial", size, "bold"))
    time.sleep(0.05)

turtle.done()
