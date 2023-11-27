import turtle
def draw_circle(t, radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_diwali_rangoli():
    screen = turtle.Screen()
    screen.bgcolor("black")

    rangoli_turtle = turtle.Turtle()
    rangoli_turtle.speed(2)

    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

    for i in range(36):
        draw_circle(rangoli_turtle, 100, colors[i % len(colors)])
        rangoli_turtle.right(10)

    rangoli_turtle.hideturtle()
    screen.mainloop()

draw_diwali_rangoli()