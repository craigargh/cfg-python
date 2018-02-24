import turtle
from random import randint

angle = randint(45, 90)

for length in range(200):
    turtle.forward(length)
    turtle.right(angle)

turtle.done()
