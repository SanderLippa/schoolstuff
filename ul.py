from turtle import *
from random import randint
ml = input("kas sa maletad oma unenagu? ")
if ml == ("jah"):
    vrv = input("mis varvi oli su unenagu? ")
    kuju = input("mis kujuga oli tegelane? ")
    ptvrv = input("mis varvi oli tegelane? ")
if ml == ("ei"):
    rand = randint(1,3)
    if rand == 1:
        vrv = ("blue")
    elif rand == 2:
        vrv = ("red")
    elif rand == 3:
        vrv = ("green")
    rand2 = randint(1,3)
    if rand2 == 1:
        ptvrv = ("yellow")
    elif rand2 == 2:
        ptvrv = ("white")
    elif rand2 == 3:
        ptvrv = ("blue")
    rand3 = randint(1,4)
    if rand3 == 1:
        kuju = ("ruut")
    elif rand3 == 2:
        kuju = ("ristkulik")
    elif rand3 == 3:
        kuju = ("ring")
    elif rand3 == 4:
        kuju = ("kolmnurk")
setup(300,300)
bgcolor(vrv)
fillcolor(ptvrv)
if kuju == ("ring"):
    begin_fill()
    circle(50,360)
    end_fill()
elif kuju == ("ruut"):
    begin_fill()
    fd(50)
    right(90)
    fd(50)
    right(90)
    fd(50)
    right(90)
    fd(50)
    end_fill()
elif kuju == ("ristkulik"):
    begin_fill()
    fd(100)
    right(90)
    fd(50)
    right(90)
    fd(100)
    right(90)
    fd(50)
    end_fill()
elif kuju == ("kolmnurk"):
    begin_fill()
    fd(100)
    left(120)
    fd(100)
    left(120)
    fd(100)
    end_fill()
hideturtle()
exitonclick()