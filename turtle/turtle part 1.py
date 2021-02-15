import turtle


def superman():
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)


def square():
    turtle.shape('turtle')
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)


def circle():
    turtle.shape('turtle')
    x = 1
    while x != 10:
        turtle.forward(x)
        turtle.left(x)
        x += 0.1


def ten_squares():
    turtle.shape('turtle')
    for i in range(1, 11):
        turtle.pendown()
        turtle.forward(i * 20)
        turtle.left(90)
        turtle.forward(i * 20)
        turtle.left(90)
        turtle.forward(i * 20)
        turtle.left(90)
        turtle.forward(i * 20)
        turtle.left(90)
        turtle.penup()
        turtle.goto(i * -10, i * -10)


def spider():
    turtle.shape('turtle')
    for _ in range(12):
        turtle.forward(100)
        turtle.stamp()
        turtle.backward(100)
        turtle.left(30)


