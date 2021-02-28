import turtle
from random import *


def brownian_motion():
    for _ in range(1000000):
        turtle.shape('turtle')
        turtle.color('red')
        turtle.forward(randint(20, 50))
        turtle.left(randint(0, 360))

brownian_motion()
