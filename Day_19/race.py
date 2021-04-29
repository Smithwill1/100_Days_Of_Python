from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour:")
y_positions = [-70, -40, -10, 20, 50, 80]
t_colours = ["red", "green", "blue", "orange", "yellow", "purple"]
all_turtles = []


for turtle_index in range(0, 6):
    bob = Turtle(shape="turtle")
    bob.pu()
    bob.goto(x=-230, y=y_positions[turtle_index])
    bob.color(t_colours[turtle_index])
    all_turtles.append(bob)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle finished first!")
            else:
                print(f"You've lost! The {winning_colour} turtle finished first!")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
