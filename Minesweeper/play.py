from minesweeper import Minesweeper 

if __name__ == "__main__":
    minesweeper = Minesweeper(10, 10, 10)
    minesweeper.print_board()

    while not minesweeper.is_completed :
        pair = input("Enter the cell like row,col: ").split(",")
        x,y = int(pair[0]), int(pair[1])
        minesweeper.play(x,y)
        minesweeper.print_board()
