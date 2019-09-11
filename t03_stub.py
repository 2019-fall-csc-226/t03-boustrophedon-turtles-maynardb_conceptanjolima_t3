#################################################################################
# Author:Ben, Concepta
# Username:maynardb, mjolimac
#
# Assignment: T03: Boustrophedon Turtles and Functions
# Purpose: To draw a square and fill it in with a boustrophedon pattern
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def outside_square(t, l):
    """
    creates a border square
    param t: a turtle object
    param l:the length of the square
    return: none
    """
    for i in range(4):
        t.forward(l)
        t.left(90)

    # ...


def draw_pattern(t, l, h):
    """
    draw the pattern inside the border square

    param t: turtle input
    param l: length of the inside design
    param h: height of the design
    return: none
    """
    for i in range(11):
        t.forward(l)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.forward(l)
        t.right(90)
        t.forward(h)
        t.right(90)
    # ...


def main():
    """
    sets up attributes and calls functions

    return: none
    """
    # ...
    wn = turtle.Screen()
    scott = turtle.Turtle()
    scott.pensize(20)
    scott.penup()
    scott.setpos(250, 250)
    scott.left(180)
    scott.pendown()

    outside_square(scott, 500)              # Function call to function_1
    scott.penup()
    scott.setposition(230, 230)
    scott.pendown()
    scott.color("red")
    draw_pattern(scott, 460, 20)            # Function call to function_2
    scott.forward(460)
    scott.left(90)
    scott.forward(20)
    scott.left(90)
    scott.forward(460)

    wn.exitonclick()


main()

