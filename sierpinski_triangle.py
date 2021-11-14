from tkinter import *
import time

root = Tk()
root.title("Serpinski Triangle")

canvas = Canvas(root, width=800, height=800)
canvas.pack()


def draw(x1, y1, x2, y2, x3, y3, depth):
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="", outline="NavyBlue")

    if depth > 0:
        x12 = (x1 + x2) / 2
        y12 = (y1 + y2) / 2
        x13 = (x1 + x3) / 2
        y13 = (y1 + y3) / 2
        x23 = (x2 + x3) / 2
        y23 = (y2 + y3) / 2

        draw(x1, y1, x12, y12, x13, y13, depth - 1)
        draw(x2, y2, x12, y12, x23, y23, depth - 1)
        draw(x3, y3, x13, y13, x23, y23, depth - 1)


while True:
    for depth in range(0, 9):
        canvas.delete("all")
        draw(50, 50, 100, 700, 700, 340, depth)
        root.update()
        time.sleep(1)
    time.sleep(2)
