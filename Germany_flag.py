import turtle

screen = turtle.Screen()
screen.setup(width=900, height=600)  
screen.title("germany_flag")

t = turtle.Turtle()

t.speed(3) 

def draw_rectangle(color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    
    for _ in range(2):
        t.forward(750) 
        t.right(90)
        t.forward(130)  
        t.right(90)
        
    t.end_fill()

draw_rectangle("black", -375, 195)
draw_rectangle("red", -375, 65)
draw_rectangle("gold", -375, -65)

t.hideturtle()
turtle.done()

# germany
