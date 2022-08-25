import turtle

mainTurtle = turtle.Turtle()
def ksusha(x,y):
    mainTurtle.penup()
    mainTurtle.pencolor('red')
    mainTurtle.goto(x,y)
    mainTurtle.pendown()
    mainTurtle.forward(50)
    mainTurtle.left(72)
    mainTurtle.forward(50)
    mainTurtle.left(72)
    mainTurtle.forward(50)
    mainTurtle.left(72)
    mainTurtle.forward(50)
    mainTurtle.left(72)
    mainTurtle.forward(50)
ksusha(x=-50, y=-0)

mainTurtle.hideturtle()
turtle.exitonclick()