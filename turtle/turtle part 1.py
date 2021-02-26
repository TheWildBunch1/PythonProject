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
    for _ in range(3):
        turtle.circle(50)
        turtle.right(180)
        turtle.circle(50)
        turtle.right(120)


def butterfly():
    turtle.shape('turtle')
    turtle.right(90)
    for i in range(1, 11):
        turtle.circle(50 + 10 * i)
        turtle.circle(-50 - 10 * i)


def spring():
    turtle.shape('turtle')
    turtle.left(90)
    for _ in range(5):
        turtle.circle(-50, 90)
        turtle.circle(-50, 90)
        turtle.circle(-10, 90)
        turtle.circle(-10, 90)


def smile():
    turtle.shape('turtle')
    turtle.up()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.down()
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    turtle.up()
    turtle.goto(-30, 80)
    turtle.down()
    turtle.color('blue')
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.up()
    turtle.forward(60)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.up()
    turtle.right(90)
    turtle.goto(0, 60)
    turtle.down()
    turtle.color('black')
    turtle.width(10)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.goto(50, 40)
    turtle.color('red')
    turtle.pendown()
    turtle.circle(-50, 90)
    turtle.circle(-50, 90)


def star(n, long):  # функция рисует звезду с n углами, длина отрезков long
    for i in range(n):
        turtle.shape('turtle')
        turtle.forward(long)
        turtle.right(n // 2 * 360 / n)