from tkinter import *
import time
import random

root = Tk()
root.title("Depth-first Search Algorithm")
root.geometry('2560x1440')
canvas = Canvas(root, width=2560, height=1440)
canvas.pack()

sx, sy = 300, 150
size = 6
bx, by = 10, 10

b = 1  # border
w = 1  # width


canvas.create_rectangle(bx, by, bx+sx*size, by+sy*size, fill="white")


def close():
    root.quit()
    root.destroy()


def draw_connection(cell1, cell2, color):
    canvas.create_line(bx + size * (cell1[1] + 0.5), by + size * (cell1[0] + 0.5), bx + size * (cell2[1] + 0.5),
                       by + size * (cell2[0] + 0.5), width=size-1, fill=color)


vc = [[0] * sx + [1] for y in range(sy)]  # visited cells
vc.append([1] * sx)
vc[sy // 2][sx // 2] = 1
'''
maze_walls = dict()
for x1 in range(sx):
    for y1 in range(sy):
        for x2 in range(sx):
            for y2 in range(sy):
                maze_walls[frozenset([(y1, x1), (y2, x2)])] = 1
# print(maze_walls)
'''


def nec(cell):  # not end cell
    pn = []

    if vc[cell[0] - 1][cell[1]] == 0:
        pn.append((cell[0] - 1, cell[1]))

    if vc[cell[0]][cell[1] + 1] == 0:
        pn.append((cell[0], cell[1] + 1))

    if vc[cell[0] + 1][cell[1]] == 0:
        pn.append((cell[0] + 1, cell[1]))

    if vc[cell[0]][cell[1] - 1] == 0:
        pn.append((cell[0], cell[1] - 1))

    # print("pn", pn)
    return pn


#def draw_connection(cell1, cell2, c):
 #   canvas.create_line(b + size * (cell1[1] + 0.5), b + size * (cell1[0] + 0.5), b + size * (cell2[1] + 0.5), b + size * (cell2[0] + 0.5), width= 1, fill=c)
    # canvas.create_rectangle(b-w/2 + size * (cell1[1] + 0.5), b-w/2 + size * (cell1[0] + 0.5), b+w/2 + size * (cell1[1] + 0.5), b+w/2 + size * (cell1[0] + 0.5), fill="black")


cell_stack = []
cell_stack.append((sy // 2, sx // 2))


def step():
    # print(cell_stack)
    ncs = nec(cell_stack[-1])
    if ncs:
        dir = ncs[random.randrange(len(ncs))]  # next cell
        vc[dir[0]][dir[1]] = 1
        draw_connection(cell_stack[-1], dir, "blue")
        #maze_walls[frozenset([dir, cell_stack[-1]])] = 0
        cell_stack.append(dir)

    else:
        if len(cell_stack) > 1:
            draw_connection(cell_stack[-1], cell_stack[-2], "black")
        cell_stack.pop()

    if len(cell_stack) != 0:
        root.after(0, step)


step()
root.mainloop()