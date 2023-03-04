from tkinter import *
from GuiTable import GuiTable


class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.gui_table = GuiTable(self.root)
        self.solve_button = Button(self.root, text="Solve", width=7, command=self.show_result)
        self.restart_button = Button(self.root, text="Restart", width=7, command=self.restart)
        self.current_button = self.solve_button
        self.current_button.grid(row=10, column=4)
        self.instruction = Label(self.root, text="Please enter numbers between 1 and 9")
        self.instruction.grid(row=9, column=3, columnspan=3)

    def start(self):
        self.gui_table.create_entries()

    def toggle_button(self):
        self.current_button.grid_forget()
        if self.current_button == self.solve_button:
            self.current_button = self.restart_button
        elif self.current_button == self.restart_button:
            self.current_button = self.solve_button
        self.current_button.grid(row=10, column=4)

    def show_result(self):
        self.gui_table.get_values_from_entries()
        self.gui_table.leave_only_errors()
        self.gui_table.hide_entries()
        self.gui_table.solve()
        self.gui_table.show_sudoku_table()
        self.toggle_button()

    def restart(self):
        self.gui_table.reset()
        self.gui_table.hide_labels()
        self.gui_table.show_entries()
        self.toggle_button()
