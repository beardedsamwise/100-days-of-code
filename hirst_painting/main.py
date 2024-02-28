import turtle as t
import random

# vars
RGB_COLORS = [
    (54, 149, 108),
    (225, 108, 201),
    (134, 58, 85),
    (224, 62, 141),
    (197, 171, 144),
    (143, 206, 180),
    (137, 106, 82),
    (210, 68, 90)
]
y = -250

# settings and object instantiation
lance = t.Turtle()
lance.shape("blank")
lance.speed("fastest")
screen = t.Screen()
t.colormode(255)

# pen up and set start position
lance.pu()
lance.teleport(-250, y)


def random_color():
    return random.choice(RGB_COLORS)


def draw_dot():
    lance.dot(20, random_color())
    lance.fd(50)


for _ in range(10):
    for _ in range(10):
        draw_dot()
    y += 50
    lance.teleport(-250, y)

screen.exitonclick()
