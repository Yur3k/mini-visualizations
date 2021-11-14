from tkinter import *
import random

root = Tk()
root.title("Sidewinder algorithm")
root.geometry('2560x1440')
canvas = Canvas(root, width=2560, height=1440)
canvas.pack()

sx, sy = 79, 125
size = 16
bx, by = 2, 2  # border
x = 0
# side = int(input())
side = 8
print("ok")

for i in range(sx+1):
    canvas.create_line(bx, size*i+by, size*sy+bx, size*i+by)
for i in range(sy+1):
    canvas.create_line(size*i+bx, by, size*i+bx, size*sx+by)


def close():
    root.quit()
    root.destroy()


def draw_connection(cell1, cell2):
    canvas.create_line(bx + size * (cell1[0] + 0.5), by + size * (cell1[1] + 0.5), bx + size * (cell2[0] + 0.5),
                       by + size * (cell2[1] + 0.5), width=size-1, fill="white")


def new_row():
    global x

    borders = [0]
    for iu in range(1, sx):
        if random.randrange(side) == 0:
            borders.append(iu)
    borders.append(sx)

    for iu in range(len(borders) - 1):
        b1, b2 = borders[iu], borders[iu+1]  # border1, border2

        draw_connection((x, b1), (x, b2-1))

        bridge = random.randrange(b1, b2)
        draw_connection((x, bridge), (x+1, bridge))

    x += 1
    root.after(100, new_row)


new_row()
mainloop()
