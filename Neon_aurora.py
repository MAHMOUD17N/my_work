import turtle
import colorsys

def draw_fractal(t, length, depth, hue):
    if depth == 0:
        return

    color = colorsys.hsv_to_rgb(hue % 1.0, 0.8, 1.0)
    t.pencolor(color)
    t.width(depth)
    t.forward(length)

    for angle in [-45, 0, 45]:
        t.left(angle)
        draw_fractal(t, length * 0.6, depth - 1, hue + 0.1)
        t.right(angle)

    t.penup()
    t.backward(length)
    t.pendown()

def main():
    screen = turtle.Screen()
    screen.setup(width=900, height=800)
    screen.bgcolor("black")
    
    screen.tracer(2)  

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    for _ in range(8):
        draw_fractal(t, 150, 5, 0.6)
        t.left(45)

    screen.update()
    turtle.done()

if __name__ == "__main__":
    main()

# neon
