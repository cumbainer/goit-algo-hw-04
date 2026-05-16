import turtle


def koch(t, length, level):
    if level == 0:
        t.forward(length)
        return
    length /= 3
    koch(t, length, level - 1)
    t.left(60)
    koch(t, length, level - 1)
    t.right(120)
    koch(t, length, level - 1)
    t.left(60)
    koch(t, length, level - 1)


def snowflake(level, size=300):
    screen = turtle.Screen()
    screen.title(f"Сніжинка Коха — рівень {level}")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()
    for _ in range(3):
        koch(t, size, level)
        t.right(120)
    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    level = int(input("Рівень рекурсії (0–5): "))
    snowflake(level)