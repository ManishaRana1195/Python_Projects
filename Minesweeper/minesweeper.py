import random


class Minesweeper:

    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.board = [[" " for _ in range(rows)] for _ in range(cols)]
        self.hidden_state = [[False for _ in range(rows)] for _ in range(cols)]
        self.exposed_cells = set()
        self.mine_cells = self.place_mines(mines)

    def place_mines(self, mine_count):
        temp = set()
        while mine_count != 0:
            pair = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
            temp.add(pair)
            self.board[pair[0]][pair[1]] = "*"
            mine_count -= 1
        self.set_nearby_mines()
        return temp

    def get_nearby_mines(self, r, c, dirs):
        nearby_mines = 0
        for dir in dirs:
            new_row = r + dir[0]
            new_col = c + dir[1]
            if new_row < 0 or new_row >= self.rows or new_col < 0 or new_col >= self.cols :
                continue
            if self.board[new_row][new_col] == "*":
                nearby_mines += 1
        return nearby_mines

    def set_nearby_mines(self):
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, -1), (-1, 1), (-1, -1), (1, 1)]
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == "*" or self.board[r][c] != " ":
                    continue
                self.board[r][c] = self.get_nearby_mines(r, c, dirs)

    def is_lost(self):
        for mine in self.mine_cells:
            self.hidden_state[mine[0]][mine[1]] = False
        print("You lost!!")
        

    def is_won(self):
        # check if all non mine calls are exposed
        if self.rows* self.cols == len(self.exposed_cells)+len(self.mine_cells):
            print("YOU WON!!")

    def play(self, row, col):
        # if self.board[row][col] == "*":
        #     self.is_lost()
        # elif self.board[row][col] != 0:
        #     self.hidden_state[row][col] = False
        #     self.is_won()
        # else :
        #     #recursively open all non * cells
        #     self.is_won()
        pass
            

    def print_board(self):
        print("")
        for i in range(self.rows):
            print(i, end="")
            for j in range(self.cols):
                if self.hidden_state[i][j]:
                    print(f"|  ", end="")
                else:
                    print(f"| {self.board[i][j]} ", end="")
            print(" |")
        print("")
