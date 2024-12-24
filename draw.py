import tkinter as tk
import numpy as np

def generate_array():
    global grid
    array = []
    for row in grid:
        for cell in row:
            array.append(cell["state"])
    print("Generated array:", array)
    return array

def fill_cell(event):
    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE
    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
        cell = grid[row][col]
        cell["state"] = 1
        color = "black"
        canvas.itemconfig(cell["rect"], fill=color)

def clear_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            cell = grid[i][j]
            cell["state"] = 0
            color = "white"
            canvas.itemconfig(cell["rect"], fill=color)


GRID_SIZE = 28
CELL_SIZE = 20

grid = []

root = tk.Tk()
root.title("28x28 Drawing Grid")

canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE, bg="white")
canvas.pack()

# Create grid of cells
for row in range(GRID_SIZE):
    grid_row = []
    for col in range(GRID_SIZE):
        x1, y1 = col * CELL_SIZE, row * CELL_SIZE
        x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
        rect = canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="gray")
        grid_row.append({"rect": rect, "state": 0})
    grid.append(grid_row)

canvas.bind("<Button-1>", fill_cell)
canvas.bind("<B1-Motion>", fill_cell)

frame = tk.Frame(root)
button1 = tk.Button(frame, text="Generate Array", command=generate_array)
button2 = tk.Button(frame, text="Clear Grid", command=clear_grid)
frame.pack(side="bottom")
button1.pack(side="left")
button2.pack(side="right")

root.mainloop()
