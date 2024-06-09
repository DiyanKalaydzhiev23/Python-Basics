import turtle

t = turtle.Pen()
turtle.bgcolor('black')

t.pencolor("red")
COLORS_COUNT = 6

for x in range(360):

    if x % COLORS_COUNT == 0:
        t.pencolor("red")
    elif x % COLORS_COUNT == 1:
        t.pencolor("purple")
    elif x % COLORS_COUNT == 2:
        t.pencolor("blue")
    elif x % COLORS_COUNT == 3:
        t.pencolor("green")
    elif x % COLORS_COUNT == 4:
        t.pencolor("yellow")
    elif x % COLORS_COUNT == 5:
        t.pencolor("orange")

    t.width(x // 100 + 1)  # increase pen size
    t.forward(x) # draw a line
    t.left(59)  # rotate 59 degrees left

