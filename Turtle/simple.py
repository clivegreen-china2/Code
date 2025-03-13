import turtle

turtle.setup(800, 800)
window = turtle.Screen()
window.bgcolor("black")
window.title("Simple Square")
my_pen = turtle.Turtle()
my_pen.speed(0)
my_pen.hideturtle()

my_pen.goto(-300, 300)
my_pen.fillcolor('green')
my_pen.down()
my_pen.begin_fill()
for i in range(4):
    my_pen.forward(300)
    my_pen.right(90)
my_pen.penup()
my_pen.end_fill()

my_pen.goto(0, 300)
my_pen.fillcolor('yellow')
my_pen.down()
my_pen.begin_fill()
for i in range(3):
    my_pen.forward(300)
    my_pen.right(90)
my_pen.penup()
my_pen.end_fill()

turtle.done()
