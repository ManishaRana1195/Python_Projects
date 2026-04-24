from player import HumanPlayer, ComputerPlayer
import time

class TicTacToe:

    def __init__(self):
        # board to keep track existing state
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        # list of tuples to track empty cells
        self.valid_moves = [(r, c) for r in range(3) for c in range(3)]

    def play(self, player):
        r, c = player.get_move(self.valid_moves)
        if self.board[r][c] == " ":
            self.board[r][c] = player.letter
            self.valid_moves.remove((r, c))
        
        return r, c

    def is_board_filled(self):
        return len(self.valid_moves) == 0

    def player_won(self, player, r, c):
        letter = player.letter
        # Check same row
        if all(letter == self.board[i][c] for i in range(3)):
            return True
        # Check same column
        if all(letter == self.board[r][i] for i in range(3)):
            return True
        # Check diagonal (top-left to bottom-right)
        if r == c:
            if all(letter == self.board[i][i] for i in range(3)):
                return True
        # Check diagonal (top-right to bottom-left)
        if r + c == 2:
            if all(letter == self.board[i][2 - i] for i in range(3)):
                return True

        return False

    def print_board(self):
        for row in range(3):
            for col in range(3):
                print(f"| {self.board[row][col]} ", end="")
            print("|")


if __name__ == "__main__":
    ticTacToe = TicTacToe()
    human_player_turn = False
    human_player = HumanPlayer("X")
    compluter_player = ComputerPlayer("O")
    player = None
    player_won = False

    print("You are X, Computer is 0.")
    while not ticTacToe.is_board_filled():
        if human_player_turn:
            human_player_turn = False
            player = human_player
        else:
            human_player_turn = True
            player = compluter_player
            print("Computer's turn")
            print("Thinking... ")
            time.sleep(5) 

        r, c = ticTacToe.play(player)
        ticTacToe.print_board()

        if ticTacToe.player_won(player, r, c):
            player_won = True
            player.won()
            break
       
    if not player_won:
        print("The game is a tie.")
