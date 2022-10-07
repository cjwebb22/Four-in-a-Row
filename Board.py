class Board:
    """
    This class represents the board.
    """    
    def __init__(self):
        """
        Initialising board.
        """
        self.rows = 6
        self.columns = 7
        row_of_board = ["0"] * self.columns
        self.board = []
        for _ in range(self.rows):
            self.board.append(row_of_board[:])
    
    def __str__(self):
        """
        Creating board string.
        """
        return_string = ""
        for row in reversed(self.board): #add each row of board to return_string in reverse
            return_string += "".join(row)
            return_string += "\n"
        return_string += "-" * self.columns #add divider to return_string
        return_string += "\n"
        for i in range(1, self.columns + 1): #add column numbers to return_string
            return_string += str(i)
        return return_string
    
    def put_in_column(self, player: str, column: int) -> (bool, str):
        """
        Puts token in column.
        
        Arguments:
        - player: a string representing the player placing the token
        - column: an integer representing the column the token is being placed

        Returns a boolean represening whether or not it was placed
        """
        if player != "1" and player != "2": #check if player is valid input
            return False
        if not column - 1 in range(self.columns): #check if column is valid input
            return False
        for row in self.board: #place token in first row to be free in column
            if row[column - 1] == "0":
                row[column - 1] = player
                return True
        return False

    def check_winner(self, player: str)-> bool:
        """
        Checks if there's a winner.

        Arguments:
        - player: a string

        Returns a boolean vale representing whether the player won.
        """
        #check for vertical win
        for C in range(self.columns):
            for i in range(self.rows-3):
                if self.board[i][C] == player and self.board[i+1][C] == player and self.board[i+2][C] == player and self.board[i+3][C] == player:
                    return True 
        
        #check for horizontal win
        for row in self.board:
            for i in range(self.columns - 3):
                if row[i] == player and row[i+1] == player and row[i+2] == player and row[i+3] == player:
                    return True              
        
        #check for diagonal win
        for i in range(self.columns-3):
            for j in range(self.rows-3):
                if self.board[j][i] == player and self.board[j+1][i+1] == player and self.board[j+2][i+2] == player and self.board[j+3][i+3] == player:
                    return True
                elif self.board[j+3][i] == player and self.board[j+2][i+1] == player and self.board[j+1][i+2] == player and self.board[j][i+3] == player:
                    return True
        
        return False
    
    def is_full(self) -> bool:
        """
        Determines if board is full.
        """
        if "0" in self.board[-1]:
            return False
        else:
            return True
                



    
