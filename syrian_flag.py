import turtle

screen = turtle.Screen()
screen.setup(width=800, height=500)
screen.bgcolor("lightgray")  

t = turtle.Turtle()
t.speed(3)
t.hideturtle()
t.penup()


def draw_rectangle(color, x, y, width, height):
    t.goto(x, y)
    t.setheading(0)

    t.fillcolor(color)
    t.pencolor("black")  
    t.pensize(0)        

    t.begin_fill()
    t.pendown()

    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

    t.end_fill()
    t.penup()


draw_rectangle("green", -300, 100, 600, 100)
draw_rectangle("white", -300, 0, 600, 100)
draw_rectangle("black", -300, -100, 600, 100)


def draw_star(x, y, color):
    t.goto(x, y)
    t.setheading(0)

    t.fillcolor(color)
    t.pencolor("red")

    t.begin_fill()
    t.pendown()

    for _ in range(5):
        t.forward(35)
        t.right(144)

    t.end_fill()
    t.penup()

draw_star(-100, -50, "red")
draw_star(0, -50, "red")
draw_star(100, -50, "red")

turtle.done()

# syria
