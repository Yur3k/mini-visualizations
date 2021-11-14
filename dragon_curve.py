from tkinter import *
import time

root = Tk()
root.title("Dragon Curve")

canvas = Canvas(root, width=1500, height=1000)
canvas.pack()


def draw(x1, y1, x2, y2, depth):
    # if depth == size - 1:
    #     canvas.create_line(x1, y1, x2, y2)

    if depth == 0:
        canvas.create_line(x1, y1, x2, y2)  # , width=3)
        return

    if x1 == x2:
        if y1 > y2:
            draw(x1, y1, x1 - abs(y2 - y1) / 2, (y1 + y2) / 2, depth - 1)
            draw(x2, y2, x1 - abs(y1 - y2) / 2, (y1 + y2) / 2, depth - 1)
        else:
            draw(x1, y1, x1 + abs(y2 - y1) / 2, (y1 + y2) / 2, depth - 1)
            draw(x2, y2, x1 + abs(y1 - y2) / 2, (y1 + y2) / 2, depth - 1)

    elif y1 == y2:
        if x1 < x2:
            draw(x1, y1, (x1 + x2) / 2, y1 - abs(x2 - x1) / 2, depth - 1)
            draw(x2, y2, (x1 + x2) / 2, y1 - abs(x2 - x1) / 2, depth - 1)
        else:
            draw(x1, y1, (x1 + x2) / 2, y1 + abs(x2 - x1) / 2, depth - 1)
            draw(x2, y2, (x1 + x2) / 2, y1 + abs(x2 - x1) / 2, depth - 1)
    else:
        if x1 < x2:
            if y1 > y2:
                draw(x1, y1, x1, y2, depth - 1)
                draw(x2, y2, x1, y2, depth - 1)
            else:
                draw(x1, y1, x2, y1, depth - 1)
                draw(x2, y2, x2, y1, depth - 1)

        else:
            if y1 > y2:
                draw(x1, y1, x2, y1, depth - 1)
                draw(x2, y2, x2, y1, depth - 1)
            else:
                draw(x1, y1, x1, y2, depth - 1)
                draw(x2, y2, x1, y2, depth - 1)


while True:
    for depth in range(0, 17):
        canvas.delete("all")
        draw(400, 600, 1100, 600, depth)
        root.update()
        time.sleep(1)
    time.sleep(2)
