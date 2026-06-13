import math
import turtle

screen = turtle.Screen()
screen.bgcolor("#000000")
screen.setup(width=750, height=750)
screen.title("Sequential Geometry Clock")

t = turtle.Turtle()
t.speed(0)  
t.hideturtle()

t.up()
t.goto(0, -260)
t.down()
t.pensize(5)
t.color("#FFFFFF")
t.circle(260)

def draw_clock_sequentially():
    hour_order = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    for hour in hour_order:
        base_angle = 90 - (hour * 30)

        for minute_offset in range(5):
            current_tick_angle = base_angle - (minute_offset * 6)
            rad = math.radians(current_tick_angle)

            t.up()
            t.goto(0, 0)
            t.setheading(current_tick_angle)

            if minute_offset == 0:
                t.forward(240)
                t.down()
                t.color("#FFFFFF")
                t.pensize(4)
                t.forward(18)
            else:
                t.forward(240)
                t.down()
                t.color("#555555") 
                t.pensize(1)
                t.forward(8)

        rad_num = math.radians(base_angle)
        x_num = 215 * math.cos(rad_num)
        y_num = 215 * math.sin(rad_num) - 15

        t.up()
        t.goto(x_num, y_num)
        t.color("#FFFFFF")
        t.write(str(hour), align="center", font=("Arial", 16, "bold"))


def draw_hands():

    #clock
    t.up()
    t.goto(0, 0)
    t.setheading(150)
    t.color("#FFFFFF")  
    t.pensize(7)
    t.down()
    t.forward(120)

    #minute
    t.up()
    t.goto(0, 0)
    t.setheading(30)
    t.color("#FFFFFF")
    t.pensize(4)
    t.down()
    t.forward(190)

    #second
    t.up()
    t.goto(0, 0)
    t.setheading(270)
    t.color("#AAAAAA")
    t.pensize(2)
    t.down()
    t.forward(206)

    t.up()
    t.goto(-5, 0)
    t.color("#FFFFFF")
    t.down()
    t.begin_fill()
    t.circle(6)
    t.end_fill()


draw_clock_sequentially()
draw_hands()

screen.mainloop()

# clock
