import turtle
import random

# Changing module (colormode)
turtle.colormode(255)


# Creating a function for RGB Tuple
def color_Shades():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


# Turtle 1
tim = turtle.Turtle()
tim.speed(0)
tim.width(2)


# Method 1
# for _ in range(150):
#     tim.color(color_Shades())
#     tim.circle(100, 360)
#     tim.left(5)
#     print(tim.heading())

# Method 2
def draw_Spirograph(size_of_gap):
    for _ in range(round(360 / size_of_gap)):
        tim.color(color_Shades())
        tim.circle(100, 360)
        current_Heading = tim.heading()
        tim.setheading(current_Heading + size_of_gap)  

draw_Spirograph(3)

# Screen
screen = turtle.Screen()

# Exit 
screen.exitonclick()
