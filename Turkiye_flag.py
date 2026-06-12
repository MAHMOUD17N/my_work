import turtle

s = turtle.Screen()
s.setup(800, 500)
s.bgcolor("white")

t = turtle.Turtle()
t.speed(4)
t.hideturtle()


t.penup()
t.goto(-250, 150)
t.pendown()
t.color("#E30A17")
t.begin_fill()
for _ in range(2):
    t.forward(500)
    t.right(90)
    t.forward(300)
    t.right(90)
t.end_fill()


t.penup()
t.goto(-100, -80) 
t.color("white")
t.pendown()
t.begin_fill()
t.circle(80) 
t.end_fill()


t.penup()
t.goto(-75, -70)
t.color("#E30A17")
t.pendown()
t.begin_fill()
t.circle(70) 
t.end_fill()


t.penup()
t.goto(45, -15) 
t.setheading(162) 
t.color("white")
t.pendown()
t.begin_fill()
for _ in range(5):
    t.forward(55) 
    t.right(144)
t.end_fill()

turtle.done()

# Turkish
