import turtle
import colorsys

def draw_luminous_art():
    screen = turtle.Screen()
    screen.bgcolor("#000000")
    screen.title("Luminous Fractal Mandala")
    screen.setup(width=900, height=900)
    
    t = turtle.Turtle()
    t.speed(0)          
    turtle.tracer(10)   
    t.hideturtle()     
    hue = 0.6           
    
    for i in range(400):
        color = colorsys.hsv_to_rgb(hue, 0.9, 1)
        t.pencolor(color)
        hue += 0.0025  
        
        t.penup()
        t.goto(0, 0)
        t.setheading(i * 15)  
        t.pendown()
        
        t.forward(i * 0.5)     
        t.circle(i * 0.2, 60) 
        t.left(120)           
        t.circle(i * 0.2, 60)  
        
    turtle.update()
    screen.mainloop()

if __name__ == "__main__":
    draw_luminous_art()

# luminous art




