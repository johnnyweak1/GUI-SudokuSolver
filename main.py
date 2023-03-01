# TODO: Wyswietlic gridem tablice

from tkinter import *

tablica = [
    [0, 0, 4, 0, 5, 0, 0, 0, 0],
    [9, 0, 0, 7, 3, 4, 6, 0, 0],
    [0, 0, 3, 0, 2, 1, 0, 4, 9],
    [0, 3, 5, 0, 9, 0, 4, 8, 0],
    [0, 9, 0, 0, 0, 0, 0, 3, 0],
    [0, 7, 6, 0, 1, 0, 9, 2, 0],
    [3, 1, 0, 9, 7, 0, 2, 0, 0],
    [0, 0, 9, 1, 8, 2, 0, 0, 3],
    [0, 0, 0, 0, 6, 0, 1, 0, 0]
]


def is_valid(tab, row, col, value):
    not_in_row = value not in tab[row]
    not_in_col = value not in [row[col] for row in tab]
    not_in_subregion = True
    subregion = [row // 3 * 3, col // 3 * 3]
    for row in tab[subregion[0]:subregion[0] + 3]:
        for row_value in row[subregion[1]:subregion[1] + 3]:
            if value == row_value:
                not_in_subregion = False
    return not_in_subregion and not_in_col and not_in_col


def solve(tab, row, col):
    if row == 9:
        return True
    if col == 9:
        return solve(tab, row + 1, 0)
    elif tab[row][col] != 0:
        return solve(tab, row, col + 1)
    else:
        for i in range(1, 10):
            if is_valid(tab, row, col, i):
                tab[row][col] = i
                if solve(tab, row, col + 1):
                    return True
                tab[row][col] = 0
        return False


def print_tab(tab):
    for row in tab:
        print(row)


solve(tablica, 0, 0)
print_tab(tablica)

def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))

root = Tk()
window_size = 726
root.geometry(f'{str(window_size)}x{str(window_size)}+600+200')
root.resizable(False, False)
canvas = Canvas(root, width=window_size, height=window_size, background='black')
canvas.bind("<Button-1>", motion)
canvas.pack()




y1 = 80
y2 = 5
size = 80
for row in tablica:

    x1 = 5
    x2 = 80
    for value in row:
        canvas.create_rectangle(x1, y1, x2, y2, fill='white')
        x1 += size
        x2 += size
    y1 += size
    y2 += size

root.mainloop()