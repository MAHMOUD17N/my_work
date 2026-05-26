import math
from turtle import *


def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)


speed(1)
bgcolor("black")
penup()
hideturtle()
color("red")


for i in range(600):
    x = hearta(i/10) * 20
    y = heartb(i/10) * 20

    goto(x, y)
    write("I Love you", align="center", font=("Arial", 15, "bold"))
done()
