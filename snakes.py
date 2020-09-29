import random
import time
import turtle

screen = turtle.Screen()
screen.title("SNAKES AND LADDER GAME")
screen.bgcolor("lightpink")
turn = 1
count = 0
a, b, c, d = 0, 0, 0, 0
tur = 0

screen.setup(900, 600)
screen.bgpic("sal.png")
move_speed = 30
turn_speed = 90

P1 = turtle.Turtle()
a1 = turtle.Turtle()
a1.up()
a1.ht()
a1.setpos(-490, -355)
P1.shape("circle")
P1.color("red")
P1.up()
P1.setpos(-370, -350)

P2 = turtle.Turtle()
a2 = turtle.Turtle()
a2.up()
a2.ht()
a2.setpos(-490, -330)
P2.shape("circle")
P2.color("blue")
P2.up()
P2.setpos(-370, -325)

P3 = turtle.Turtle()
a3 = turtle.Turtle()
a3.up()
a3.ht()
a3.setpos(-490, -305)
P3.shape("circle")
P3.color("green")
P3.up()
P3.setpos(-370, -300)

P4 = turtle.Turtle()
a4 = turtle.Turtle()
a4.up()
a4.ht()
a4.setpos(-490, -280)
P4.shape("circle")
P4.color("yellow")
P4.up()
P4.setpos(-370, -275)

# speed
P1.speed(1)
P2.speed(1)
P3.speed(1)
P4.speed(1)

dc = 6
image = str(dc) + ".gif"
Dice = turtle.Turtle()
screen.addshape(image)
Dice.shape(image)
Dice.ht()
Dice.up()
Dice.speed(0)
Dice.clear()
Dice.setpos(-500, 300)
Dice.st()


def fn(x, y):
    global dc, turn, a, b, c, d, count
    if x <= -480.0 and x >= -600.0 and y >= 250.0 and y <= 350.0:
        i = 0
        while i < 10:
            dc = random.randint(1, 6)
            image = str(dc) + ".gif"
            Dice = turtle.Turtle()
            screen.addshape(image)
            Dice.shape(image)
            Dice.ht()
            Dice.up()
            Dice.speed(0)
            Dice.setpos(-500, 300)
            screen.update()
            Dice.clear()
            Dice.st()
            i += 1

        if a == 100:
            style = ("Arial", 16, "bold")
            turtle.undo()
            turtle.write("Player1 win", font=style)

        elif b == 100:
            style = ("Arial", 16, "bold")
            turtle.undo()
            turtle.write("Player2 win", font=style)
        elif c == 100:
            style = ("Arial", 16, "bold")
            turtle.undo()
            turtle.write("Player3 win", font=style)
        elif d == 100:
            style = ("Arial", 16, "bold")
            turtle.undo()
            turtle.write("Player4 win", font=style)

        move()
    else:
        dice()


def forward():
    global turn, a, b, c, d, tur
    m = dc
    P = 0
    if turn == 1:
        tur = a
        P = P1
    elif turn == 2:
        tur = b
        P = P2
    elif turn == 3:
        tur = c
        P = P3
    elif turn == 4:
        tur = d
        P = P4
    for i in range(dc):
        if tur % 10 == 0 and tur % 20 != 0 and tur + m > tur:
            P.left(90)
            P.fd(70)
            P.left(90)
        if tur % 20 == 0 and tur + m > tur:
            P.right(90)
            P.fd(70)
            P.right(90)
        if tur % 10 != 0:
            P.forward(70)
        tur += 1
        m -= 1
    if turn == 1 and a + dc <= 100:
        a += dc
    elif turn == 2 and b + dc <= 100:
        b += dc
    elif turn == 3 and c + dc <= 100:
        c += dc
    elif turn == 4 and d + dc <= 100:
        d += dc
    # stairs
    if a == 4:
        P1.setpos(-35, 10)
        P1.left(180)
        a = 56
    if b == 4:
        P2.setpos(-35, 10)
        P2.left(180)
        b = 56
    if c == 4:
        P3.setpos(-35, 10)
        P3.left(180)
        c = 56
    if d == 4:
        P4.setpos(-35, 10)
        P4.left(180)
        d = 56

    if a == 14:
        P1.setpos(35, 10)
        a = 55
    if b == 14:
        P2.setpos(35, 10)
        b = 55
    if c == 14:
        P3.setpos(35, 10)
        c = 55
    if d == 14:
        P4.setpos(35, 10)
        d = 55

    if a == 12:
        P1.setpos(315, -60)
        P1.right(180)
        a = 50
    if b == 12:
        P2.setpos(315, -60)
        P2.right(180)
        b = 50
    if c == 12:
        P3.setpos(315, -60)
        P3.right(180)
        c = 50
    if d == 12:
        P4.setpos(315, -60)
        P4.right(180)
        d = 50

    if a == 22:
        P1.setpos(-175, 10)
        P1.left(180)
        a = 58
    if b == 22:
        P2.setpos(-175, 10)
        P2.left(180)
        b = 78
    if c == 22:
        P3.setpos(-175, 10)
        P3.left(180)
        c = 58
    if d == 22:
        P4.setpos(-175, 10)
        P4.left(180)
        d = 58

    if a == 41:
        P1.setpos(-245, 150)
        P1.left(180)
        a = 79
    if b == 41:
        P2.setpos(-245, 150)
        P2.left(180)
        b = 79
    if c == 41:
        P3.setpos(-245, 150)
        P3.left(180)
        c = 79
    if d == 41:
        P4.setpos(-245, 150)
        P4.left(180)
        d = 79

    if a == 54:
        P1.setpos(175, 220)
        P1.right(180)
        a = 88
    if b == 54:
        P2.setpos(175, 220)
        P2.right(180)
        b = 88
    if c == 54:
        P3.setpos(175, 220)
        P3.right(180)
        c = 88
    if d == 54:
        P4.setpos(175, 220)
        P4.right(180)
        d = 88

    # snakes
    if a == 96:
        P1.setpos(-245, -60)
        P1.right(180)
        a = 42
    if b == 96:
        P2.setpos(-245, -60)
        P2.right(180)
        b = 42
    if c == 96:
        P3.setpos(-245, -60)
        P3.right(180)
        c = 42
    if d == 96:
        P4.setpos(-245, -60)
        P4.right(180)
        d = 42

    if a == 94:
        P1.setpos(315, 150)
        a = 71
    if b == 94:
        P2.setpos(315, 150)
        b = 71
    if c == 94:
        P3.setpos(315, 150)
        c = 71
    if d == 94:
        P4.setpos(315, 150)
        d = 71

    if a == 75:
        P1.setpos(245, -130)
        a = 32
    if b == 75:
        P2.setpos(245, -130)
        b = 32
    if c == 75:
        P3.setpos(245, -130)
        c = 32
    if d == 75:
        P4.setpos(245, -130)
        d = 32

    if a == 47:
        P1.setpos(-35, -270)
        P1.left(180)
        a = 516
    if b == 47:
        P2.setpos(-35, -270)
        P2.left(180)
        b = 16
    if c == 47:
        P3.setpos(-35, -270)
        P3.left(180)
        c = 16
    if d == 47:
        P4.setpos(-35, -270)
        P4.left(180)
        d = 16

    if a == 37:
        P1.setpos(-175, -340)
        P1.right(180)
        a = 3
    if b == 37:
        P2.setpos(-175, -340)
        P2.right(180)
        b = 3
    if c == 37:
        P3.setpos(-175, -340)
        P3.right(180)
        c = 3
    if d == 37:
        P4.setpos(-175, -340)
        P4.right(180)
        d = 3

    if a == 28:
        P1.setpos(315, -340)
        a = 10
    if b == 28:
        P2.setpos(315, -340)
        b = 10
    if c == 28:
        P3.setpos(315, -340)
        c = 10
    if d == 28:
        P4.setpos(315, -340)
        d = 10


def dice():
    turtle.ht()
    turtle.up()
    turtle.setpos(-590, 350)
    style = ("Arial", 16, "bold")
    turtle.write("Click on Dice to Roll", font=style)
    screen.onclick(fn)


def decision():
    global turn, count, a, b, c, d
    if dc == 6 and count < 3:
        count += 1
        forward()
        dice()
    elif dc != 6:
        if turn == 1:
            forward()
            a1.undo()
            p2()
        elif turn == 2:
            forward()
            a2.undo()
            p3()
        elif turn == 3:
            forward()
            a3.undo()
            p4()
        elif turn == 4:
            forward()
            a4.undo()
            p1()
    if count == 3:
        count = 0
        if turn == 1:
            a -= 12
            a1.undo()
            p2()
        elif turn == 2:
            b -= 12
            a2.undo()
            p3()
        elif turn == 3:
            c -= 12
            a3.undo()
            p4()
        elif turn == 4:
            d -= 12
            a4.undo()
            p1()


def move():
    global turn, count, a, b, c, d
    if turn == 1 and a == 0 and dc == 6:
        P1.setpos(-315, -340)
        a = 1
        count += 1
        dice()
    elif turn == 1 and a != 0:
        decision()
    elif turn == 1:
        a1.undo()
        p2()

    elif turn == 2 and b == 0 and dc == 6:
        P2.setpos(-315, -340)
        b = 1
        count += 1
        dice()
    elif turn == 2 and b != 0:
        decision()
    elif turn == 2:
        a2.undo()
        p3()

    elif turn == 3 and c == 0 and dc == 6:
        P3.setpos(-315, -340)
        c = 1
        count += 1
        dice()
    elif turn == 3 and c != 0:
        decision()
    elif turn == 3:
        a3.undo()
        p4()
    elif turn == 4 and d == 0 and dc == 6:
        P4.setpos(-315, -340)
        d = 1
        count += 1
        dice()
    elif turn == 4 and d != 0:
        decision()
    elif turn == 4:
        a4.undo()
        p1()


def p1():
    global turn, count, a
    count = 0
    turn = 1
    style = ("Arial", 10, "bold")
    a1.write("Player 1 Turn-->", font=style)
    dice()
    print(a)


def p2():
    global turn, count, b
    count = 0
    turn = 2
    style = ("Arial", 10, "bold")
    a2.write("Player 2 Turn-->", font=style)
    dice()
    print(b)


def p3():
    global turn, count, c
    count = 0
    turn = 3
    style = ("Arial", 10, "bold")
    a3.write("Player 3 Turn-->", font=style)
    dice()
    print(d)


def p4():
    global count, turn, d
    count = 0
    turn = 4
    style = ("Arial", 10, "bold")
    a4.write("Player 4 Turn-->", font=style)
    dice()
    print(d)


start_time = time.time()
p1()
turtle.mainloop()

print("%s seconds" % (time.time() - start_time))
