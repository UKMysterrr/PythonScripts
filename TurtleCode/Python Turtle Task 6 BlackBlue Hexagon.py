import turtle

turtle.fillcolor("Black")
turtle.pencolor("Blue")

turtle.begin_fill()

for i in range(4):
    turtle.forward(150)
    turtle.right(90)

turtle.end_fill()

while True:
    turtle.right(5)
    turtle.left(5)
