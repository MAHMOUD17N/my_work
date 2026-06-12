import subprocess
import sys
import turtle
import time


from arabic_reshaper import reshape
from bidi.algorithm import get_display


screen = turtle.Screen()
screen.title("iraq_flag")
screen.setup(width=900, height=500)
t = turtle.Turtle()
t.speed(3) 

def draw_rectangle(color, x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()


draw_rectangle("#ED0E28", -250, 150, 500, 100) # أحمر
draw_rectangle("#FFFFFF", -250, 50, 500, 100)  # أبيض
draw_rectangle("#000000", -250, -50, 500, 100) # أسود


text = "االله أكبر"
reshaped_text = reshape(text)
final_text = get_display(reshaped_text)

t.penup()
t.goto(80, -28)
t.color("#007A3D")
t.write(final_text, align="right", font=("AD-Rsail", 33, "bold"))

t.hideturtle()
screen.mainloop()

# iraq_flag
