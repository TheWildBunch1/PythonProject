import turtle
import math


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


def spiral():
    turtle.shape('turtle')
    for i in range(1000):
        turtle.forward(i * 0.001)
        turtle.left(2)


def square_spiral():
    turtle.shape('turtle')
    for i in range(1, 21):
        turtle.forward(i * 10)
        turtle.left(90)
        turtle.forward(i * 10)
        turtle.left(90)


def ten_regular_polygons():
    turtle.shape('turtle')
    n = 3
    r = 20  # задаем радиус первой окружности

    def more_angles(n, m):  # опеределяем функцию, рисующую многоугольник
        q = 360 / n
        while n > 0:
            turtle.left(q)
            turtle.forward(m)
            n -= 1

    while n < 13:
        m = 2 * r * math.sin(math.pi / n)  # считаем размер стороны многоугольника (a=2Rsin (360/2n))
        x = (180 - 360 / n) / 2
        turtle.left(x)
        more_angles(n, m)
        turtle.right(x)
        turtle.penup()
        turtle.forward(10)  # задаем расстояние м/у окружностями
        turtle.pendown()
        n += 1
        r += 10  # раз расстояние м/у окружностями 10, увеличиваем радиус на 10


def flower():
    turtle.shape('turtle')
    x = 0
    for _ in range(3):
        x = 0
        while x < 8.5:
            turtle.forward(x)
            turtle.left(x)
            x += 0.1
        x = 0
        while x < 8.5:
            turtle.forward(x)
            turtle.right(x)
            x += 0.1
        turtle.right(120)
