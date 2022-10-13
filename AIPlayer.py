from Board import Board
from copy import deepcopy
from random import choice

class AIPlayer:
    
    def __init__(self):
        """
        Initialises AIPlayer Object.
        """
        self.number = "2"
    
    def ChooseColumn(self, depth: int, board: Board) -> int:
        """
        Returns a column to play.
        """
        choices = None
        #get first potential column
        for i in range(board.columns):
            if board.board[-1][i] == "0":
                choices = [i + 1]
                score = self.minimax(depth, board, self.number, choices[0])
                break
        #iterate through the rest of the column to find choices
        for i in range(choices[0] + 1, board.columns + 1):
            if board.board[-1][i-1] == "0":
                temp = self.minimax(depth, board, self.number, i)
                if temp > score:
                    score = temp
                    choices = [i] # get rid of old choices
                elif score == temp:
                    choices.append(i)
        #return choices
        if choices != None:
            return choice(choices)
    
    def minimax(self, depth: int, board: Board, player: str, column: int) -> int:
        """
        Returns minimum or maximum score that can be achieved assuming moves made are as perfect as the depth specifies.
        """
        board = deepcopy(board)
        #return nothing if token can't be put in column
        if not board.put_in_column(player, column):
            return
        # return heuristic
        if depth <= 0:
            return 0
        elif board.check_winner(str(3 - int(self.number))):
            return -depth
        elif board.check_winner(self.number):
            return depth
        elif board.is_full():
            return 0
        # return minimum score that be achieved by next player, if player is AIPlayer
        elif player == self.number:
            best = -depth + 1
            score = 1000
            for i in range(1, board.columns+1):
                if board.board[-1][i-1] == "0":
                    temp = self.minimax(depth-1, board, str(3-int(self.number)), i)
                    if temp != None:
                        score = min(score, temp)
                    if score == best:
                        break
        # return maximum score that can be achieved by next player otherwise
        else:
            best = depth-1
            score = -1000
            for i in range(1, board.columns+1):
                if board.board[-1][i-1] == "0":
                    temp = self.minimax(depth-1, board, self.number, i)
                    if temp != None:
                        score = max(score, temp)
                    if score == best:
                        break
        return score
