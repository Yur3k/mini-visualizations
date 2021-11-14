from tkinter import *
from math import *
import time

root = Tk()
root.title("Koch Snowflake")

canvas = Canvas(root, width=1900, height=600)
canvas.pack()


# Return vector x, y rotated counterclockwise by angle 'phi'
def rotate(x, y, phi):
    # Legacy 2018 broken code
    '''
    st_angle = atan2(x, y)
    angle += st_angle

    if 2 / 3 * pi - 0.1 < angle < 2 / 3 * pi + 0.1:
        angle = 4 / 3 * pi

    r = sqrt(x * x + y * y)

    # print(angle, cos(angle) * r, sin(angle) * r)
    return cos(angle) * r, sin(angle) * r
    '''

    # A little something I came up with in Nov 2021
    # (x + y*i) * (cos_phi + sin_phi*i) = (x*cos_phi - y*sin_phi) + (x*sin_phi + y*cos_phi)*i
    # I love complex numbers SOO much!
    return x*cos(phi) - y*sin(phi), x*sin(phi) + y*cos(phi)


def draw(x1, y1, x2, y2, depth):
   # print(depth)
    if depth == 0:
        canvas.create_line(x1, y1, x2, y2, width=2)
        return

    p1x = (2 * x1 + x2) / 3
    p1y = (2 * y1 + y2) / 3
    p2x = (x1 + 2 * x2) / 3
    p2y = (y1 + 2 * y2) / 3

    p3x, p3y = rotate(p2x - p1x, p2y - p1y, pi/3)
    p3x += p1x
    p3y += p1y

    # canvas.create_polygon(p1x, p1y, p2x, p2y, p3x, p3y)

    draw(x1, y1, p1x, p1y, depth - 1)
    draw(p1x, p1y, p3x, p3y, depth - 1)
    draw(p3x, p3y, p2x, p2y, depth - 1)
    draw(p2x, p2y, x2, y2, depth - 1)

    # canvas.create_line(p1x-2, p1y, p1x+2, p1y, fill="red", width=4)
    # canvas.create_line(p2x-2, p2y, p2x+2, p2y, fill="green", width=4)
    # canvas.create_line(p3x-2, p3y, p3x+2, p3y, fill="blue", width=4)
    # print(p1x, p1y, p2x, p2y, p3x, p3y, depth)


while True:
    for depth in range(0, 8):
        canvas.delete("all")
        draw(1880, 590, 20, 590, depth)
        root.update()
        time.sleep(1)
    time.sleep(2)

# root.mainloop()

# Finally fixed this in 2021!
