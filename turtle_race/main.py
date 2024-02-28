from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
winner = ""
race_is_on = False
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
)

# create turtles
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtles.append(turtle)

# move turtles to starting positions
gap = 150 / (len(turtles) / 2)
for i in range(len(turtles)):
    turtles[i].penup()
    if i == 0:
        turtles[i].goto(-220, -150)
    else:
        y = (turtles[i - 1].ycor())
        turtles[i].goto(-220, y + gap)

# start the race!
if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 220:
            race_is_on = False
            winner = turtle.pencolor()

if user_bet == winner:
    print(f"You won! The winning turtle was {winner}")
else:
    print(f"You lost! The winning turtle was {winner}")

screen.exitonclick()
