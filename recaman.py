from tkinter import *

offset_x = 0
center_y = 500
size = 3

root = Tk()
root.title("Recaman sequence")

canvas = Canvas(root, width=1900, height=1280, background="OliveDrab2")
canvas.pack()

used = set()
step = 1
current = 0

def draw_sequence():
    global step
    global current

    used.add(current)

    if current - step in used or current < step:
        canvas.create_arc(current * size + offset_x,
                          center_y - step / 2 * size,
                          (current+step) * size + offset_x,
                          center_y + step / 2 * size,
                          style="arc", extent=180, outline="blue")
        current += step
    else:
        canvas.create_arc((current-step) * size + offset_x,
                          center_y - step / 2 * size,
                          current * size + offset_x,
                          center_y + step / 2 * size,
                          style="arc", start=180, extent=180, outline="blue")
        current -= step

    step += 1

    root.after(100, draw_sequence)


draw_sequence()

root.mainloop()
