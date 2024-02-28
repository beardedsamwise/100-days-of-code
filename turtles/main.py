import turtle as t
import random

timmy = t.Turtle()
screen = t.Screen()
t.colormode(255)
timmy.shape("turtle")
timmy.pensize(1)
timmy.speed(100)

COLOURS = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
ANGLES = [0,90,180,270]
GAP = 10

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def random_walk():
    timmy.color(random_color())
    timmy.right(random.choice(ANGLES))
    timmy.forward(50)

def random_color_circle():
    timmy.color(random_color())
    timmy.circle(100)

for _ in range(int(360 / GAP)):
    random_color_circle()
    timmy.right(GAP)

screen.exitonclick()