import turtle
turtle.bgcolor("black")


sq = turtle.Turtle()
sq.speed(20)
sq.pencolor('red')
for i in range(600):
    sq.forward(i)
    sq.left(91)
    sq.forward(12)
    sq.right(50)