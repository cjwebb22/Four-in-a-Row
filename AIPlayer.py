from Board import Board
from copy import deepcopy
from random import choice

class AIPlayer:
    
    def __init__(self):
        self.number = "2"
        self.name = "Player 2"
    
    def ChooseColumn(self, depth: int, board: Board) -> int:
        choices = None
        for i in range(board.columns):
            if board.board[-1][i] == "0":
                choices = [i + 1]
                score = self.minimax(depth, board, "2", choices[0])
                break
        for i in range(choices[0] + 1, board.columns + 1):
            if board.board[-1][i-1] == "0":
                temp = self.minimax(depth, board, "2", i)
                if temp > score:
                    score = temp
                    choices = [i]
                elif score == temp:
                    choices.append(i)
        if choices != None:
            return choice(choices)
    
    def minimax(self, depth: int, board: Board, player: str, column: int) -> int:
        board = deepcopy(board)
        if not board.put_in_column(player, column):
            return
        if depth <= 0:
            return 0
        elif board.check_winner(str(3 - int(self.number))):
            return -depth
        elif board.check_winner(self.number):
            return depth
        elif board.is_full():
            return 0
        elif player == self.number:
            best = -depth + 1
            score = 1000
            for i in range(1, board.columns+1):
                if board.board[-1][i-1] == "0":
                    score = min(score, self.minimax(depth-1, board, str(3-int(self.number)), i))
                    if score == best:
                        break
        else:
            best = depth-1
            score = -1000
            for i in range(1, board.columns+1):
                if board.board[-1][i-1] == "0":
                    score = max(score, self.minimax(depth-1, board, self.number, i))
                    if score == best:
                        break
        return score
