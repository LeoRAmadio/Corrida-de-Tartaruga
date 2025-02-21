import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow" ,"green" ,"blue" ,"purple"]

all_turtles = []

x = -230
y = -100
for color in colors:
    jabuti = Turtle("turtle")
    jabuti.color(color)
    jabuti.penup()
    jabuti.goto(x, y)
    all_turtles.append(jabuti)
    y += 45

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()

