import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, valid_moves):
        pass


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, valid_moves):
        return random.choice(valid_moves)

    def won(self):
        print("Yayee, the computer player won")


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, valid_moves):
        user_input = input("Enter your choice as shown (row,column): ")
        choice = user_input.split(",")
        return int(choice[0]), int(choice[1])

    def won(self):
        print("Yayee, the human player won")
