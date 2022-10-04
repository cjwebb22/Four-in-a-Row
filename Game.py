from Board import Board
    
class Game:
    """
    This class defines the game.
    """
    def __init__(self):
        """
        Initialises game
        """
        self.board = Board()
        self.outcome = None
        self.menu()
    
    def execute_turn(self, player):
        """
        Executes a turn.

        Arguments:
        - player : a string representing player playing

        Returns a boolean representing whether the game has ended.
        """
        #get input
        while True:
            column = input(f"Player {player} please input a column number or '.' to go back to the menu: ")
            #check if input valid
            try:
                column = int(column)
                if self.board.put_in_column(player, column):
                    break
                else:
                    print(f"Column full. Please input a column that isn't full or '.' to go back to the menu.")
            except ValueError:
                if column == ".":
                    self.outcome = "HALT"
                    break
                else:
                    print(f"Please input an integer or '.' to go back to the menu.")
        #check if halting
        if column == ".":
            return True
        print(self.board)
        #check if winner
        if self.board.check_winner(player):
            self.outcome = f"Player {player} wins!"
            return True
        #check if draw
        elif self.board.is_full():
            self.outcome = "Draw"
            return True
        return False
    
    def multiplayer_game(self):
        """
        Runs a 2 player game of connect 4.
        """
        print(self.board)
        #execute turns
        while True:
            if self.execute_turn("1"):
                break
            if self.execute_turn("2"):
                break
        print(self.outcome)

    def print_rules(self):
        """
        Prints the rules of connect 4.
        """
        #print out rules
        print("Connect 4 has pretty simple rules.")
        print("Each player enters a column number 1-7 to place a token in that column.")
        print("The first player with 4 tokens in a row (horizontally, vertically or diagonally) wins!")
        print("If the board is full and no player has won it's a draw.")
        input("Please press enter to go back.")
    
    def menu(self):
        """
        Menu for game.
        """
        while True:
            #print out game options
            print("Welcome to Connect-Four!")
            print("1. Play game")
            print("2. Display rules")
            print("3. Exit")
            #get input
            while True:
                try:
                    option = int(input("Please enter an option: "))
                    if option in range(1,4):
                        break
                except ValueError:
                    pass
                print("Invalid input.")
            #act on input
            if option == 1:
                self.multiplayer_game()
            elif option == 2:
                self.print_rules()
            else:
                print("Goodbye!")
                break
            



