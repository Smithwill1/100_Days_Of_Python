from turtle import Turtle, Screen, colormode
import random

bob = Turtle()
bob.shape("turtle")
colormode(255)
bob.speed("fastest")

colour_list = [(238, 243, 250), (235, 224, 84), (113, 179, 212), (213, 158, 111), (205, 5, 68), (235, 50, 128),
               (195, 74, 16), (194, 165, 12), (13, 22, 60), (31, 103, 167), (233, 225, 4), (28, 191, 119),
               (215, 135, 177), (17, 28, 173), (203, 31, 129), (230, 166, 199), (12, 184, 214), (119, 192, 162),
               (61, 22, 9), (35, 136, 76), (139, 219, 202), (9, 48, 26), (104, 92, 211), (188, 16, 5), (128, 218, 232),
               (238, 66, 36), (64, 12, 37)]

def square():
    for x in range(4):
        bob.fd(100)
        bob.rt(90)


def dashed_line():
    for x in range(50):
        bob.fd(10)
        bob.pu()
        bob.fd(10)
        bob.pd()


def shapes():
    sides = 3
    while sides <= 12:
        for x in range(sides):
            change_colour()
            bob.fd(100)
            bob.rt(360 / sides)
        sides += 1


def change_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


def pick_colour():
    colour = random.choice(colour_list)
    return colour


def random_walk():
    bob.width(10)
    for x in range(200):
        change_colour()
        direction = [0, 90, 180, 270]
        bob.seth(random.choice(direction))
        bob.fd(20)


def spyro(offset):
    for x in range(int(360 / offset)):
        bob.color(change_colour())
        bob.circle(150)
        bob.lt(offset)


def painting():
    bob.pu()
    dots = 10
    while dots >= 1:
        count = 0
        while count <= 2:
            for y in range(dots):
                bob.dot(20, change_colour())
                bob.fd(30)
            bob.lt(90)
            count += 1
        dots -= 1


def draw_painting():
    bob.pu()
    bob.seth(225)
    bob.fd(300)
    bob.seth(0)
    no_of_dots = 100

    for dot_count in range(1, no_of_dots + 1):
        bob.dot(20, pick_colour())
        bob.fd(50)

        if dot_count % 10 == 0:
            bob.seth(90)
            bob.fd(50)
            bob.seth(180)
            bob.fd(500)
            bob.seth(0)


draw_painting()
#painting()
#spyro(5)

screen = Screen()
screen.exitonclick()