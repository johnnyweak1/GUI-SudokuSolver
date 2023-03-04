from Table import Table
from SudokuTable import SudokuTable
from tkinter import *


class GuiTable(Table):
    def __init__(self, root):
        self.sudoku_table = SudokuTable()
        self.root = root
        self.entries = []
        self.labels = []

    def create_entries(self):
        for row in range(self.sudoku_table.get_row_num()):
            entry_row = []
            for col in range(self.sudoku_table.get_col_num()):
                entry = Entry(self.root, width=10)
                entry.grid(row=row, column=col)
                entry_row.append(entry)
                self.root.columnconfigure(col, minsize=100)
            self.entries.append(entry_row)
            self.root.rowconfigure(row, minsize=50)

    def get_values_from_entries(self):
        table = []
        for entry_row in self.entries:
            table_row = []
            for value in entry_row:
                value = value.get()
                if value == '':
                    table_row.append(0)
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        value = 'Error'
                    else:
                        if value > 9 or value < 1:
                            value = 'Error'
                    table_row.append(value)
            table.append(table_row)
        self.set_table(table)

    def set_table(self, table):
        self.sudoku_table.set_table(table)

    def solve(self):
        self.sudoku_table.solve()

    def show_sudoku_table(self):
        for row in range(self.sudoku_table.get_row_num()):
            label_row = []
            for col in range(self.sudoku_table.get_col_num()):
                label = Label(self.root, text=f"{self.sudoku_table.table[row][col]}")
                label.grid(row=row, column=col)
                label_row.append(label)
                self.root.columnconfigure(col, minsize=100)
            self.labels.append(label_row)
            self.root.rowconfigure(row, minsize=50)

    def hide_entries(self):
        for row in range(len(self.entries)):
            for col in range(len(self.entries[row])):
                self.entries[row][col].grid_forget()

    def show_entries(self):
        for row in range(len(self.entries)):
            for col in range(len(self.entries[row])):
                self.entries[row][col].grid(row=row, column=col)

    def hide_labels(self):
        for row in range(len(self.labels)):
            for col in range(len(self.labels[row])):
                self.labels[row][col].grid_forget()

    def reset(self):
        self.sudoku_table.reset_values()

    def check_values(self):
        for row in range(self.sudoku_table.get_row_num()):
            for col in range(self.sudoku_table.get_col_num()):
                if self.sudoku_table.table[row][col] == 'Error':
                    self.sudoku_table.leave_only_errors()
