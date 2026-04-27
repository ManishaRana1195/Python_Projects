class Sudoku:

    def __init__(self):
        self.size = 9
        self.row_sets = [{} for _ in range(self.size)]
        self.col_sets = [{} for _ in range(self.size)]
        self.box_sets = [{} for _ in range(self.size)]
        self.board = [[" " for i in range(self.size)] for j in range(self.size)]
        pass

    def print(self):
        print("-"*31)
        for i in range(self.size):
            for j in range(self.size):
                if j == 0:
                    print(f"| {self.board[i][j]} ", end="")
                elif (j+1)%3 == 0:
                    print(f" {self.board[i][j]} |", end="")
                else:
                    print(f" {self.board[i][j]} ", end="")
            print("")
            if (i+1)%3 == 0:
                    print("-"*31)

if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.print()