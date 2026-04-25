import random


class Minesweeper:

    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, -1), (-1, 1), (-1, -1), (1, 1)]
        self.is_completed = False
        
        self.board = [[" " for _ in range(rows)] for _ in range(cols)]
        self.hidden_state = [[True for _ in range(rows)] for _ in range(cols)]
        self.exposed_cells = set()
        self.mine_cells = self.place_mines(mines)


    def place_mines(self, mine_count):
        temp = set()
        while mine_count != 0:
            pair = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
            print(pair)
            temp.add(pair)
            self.board[pair[0]][pair[1]] = "*"
            mine_count -= 1
        self.set_nearby_mines()
        return temp


    def get_nearby_mines(self, r, c):
        nearby_mines = 0
        for dir in self.dirs:
            new_row = r + dir[0]
            new_col = c + dir[1]
            if new_row < 0 or new_row >= self.rows or new_col < 0 or new_col >= self.cols :
                continue
            if self.board[new_row][new_col] == "*":
                nearby_mines += 1
        return nearby_mines


    def set_nearby_mines(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == "*" or self.board[r][c] != " ":
                    continue
                self.board[r][c] = self.get_nearby_mines(r, c)


    def is_lost(self):
        for mine in self.mine_cells:
            self.hidden_state[mine[0]][mine[1]] = False
        self.is_completed = True
        print("You lost!!")
        

    def is_won(self):
        if self.rows* self.cols == len(self.exposed_cells)+len(self.mine_cells):
            self.is_completed = True
            print("YOU WON!!")


    def play(self, row, col):
        self.exposed_cells.add((row,col))

        if self.board[row][col] == "*":
            self.is_lost()
        elif self.board[row][col] > 0:
            self.hidden_state[row][col] = False
            self.is_won()
        else :
            self.hidden_state[row][col] = False
            for dir in self.dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]
                if new_row < 0 or new_row >= self.rows or new_col < 0 or new_col >= self.cols :
                    continue
                if (new_row, new_col) in self.exposed_cells: 
                    continue
                self.play(new_row, new_col)


    def print_board(self):
        print("")
        for i in range(self.rows):
            print(i, end="")
            for j in range(self.cols):
                if self.hidden_state[i][j]:
                    if len(self.exposed_cells) == 0:
                        print(f"|  ", end="")
                    else:
                        print(f"|   ", end="")
                else:
                    print(f"| {self.board[i][j]} ", end="")
            print(" |")
        print("")
