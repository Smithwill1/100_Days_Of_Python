from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()


def move_forward():
    bob.fd(10)


def turn_left():
    bob.lt(10)


def turn_right():
    bob.rt(10)


def move_backward():
    bob.bk(10)


def reset():
    bob.clear()
    bob.reset()



screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=reset)

screen.exitonclick()