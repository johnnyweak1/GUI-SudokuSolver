from Table import Table


class SudokuTable(Table):
    def __init__(self):
        self.table = [[0 for _ in range(9)] for _ in range(9)]

    def is_valid(self, row, col, value):
        not_in_row = value not in self.table[row]
        not_in_col = value not in [row[col] for row in self.table]
        not_in_subregion = True
        subregion = [row // 3 * 3, col // 3 * 3]
        for row in self.table[subregion[0]:subregion[0] + 3]:
            for row_value in row[subregion[1]:subregion[1] + 3]:
                if value == row_value:
                    not_in_subregion = False
        return not_in_subregion and not_in_col and not_in_row

    def solve(self, row=0, col=0):
        if row == 9:
            return True
        if col == 9:
            return self.solve(row + 1, 0)
        elif self.table[row][col] != 0:
            return self.solve(row, col + 1)
        else:
            for i in range(1, 10):
                if self.is_valid(row, col, i):
                    self.table[row][col] = i
                    if self.solve(row, col + 1):
                        return True
                    self.table[row][col] = 0
            return False

    def set_table(self, table):
        self.table = table

    def get_row_num(self):
        return len(self.table)

    def get_col_num(self):
        return len(self.table[0])

    def reset_values(self):
        self.table = [[0 for _ in range(9)] for _ in range(9)]

    def check_values(self):
        for row in range(len(self.table)):
            for col in range(len(self.table[0])):
                if self.table[row][col] != 'Error':
                    self.table[row][col] = ''
