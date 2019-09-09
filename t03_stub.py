#################################################################################
# Author:Ben, Concepta
# Username:
#
# Assignment:
# Purpose:
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
    for i in range(12):
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
    Docstring for main
    """
    # ...
    test = turtle.Turtle()
    test.penup()
    test.setpos(250, 250)
    test.left(180)
    test.pendown()

    outside_square(test, 500)            # Function call to function_1
    draw_pattern(test, 480, 40)            # Function call to function_2


main()

