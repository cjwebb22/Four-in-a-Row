from Board import Board
from copy import deepcopy
from random import choice

def AIChooseColumn(depth: int, board: Board) -> str:
    board = deepcopy(board)
    choices = None
    #get first choice to compare to
    for i in range(board.columns):
        if board.board[-1][i] == "0": #if column isn't full
            choices = [i + 1]
            score = minimax(depth, board, "2", False, choices[0])
            break
    #go through other columns
    for i in range(choices[0] + 1, board.columns + 1):
        if board.board[-1][i-1] == "0": #if column isn't full 
            temp = minimax(depth, board, "2", False, i)
            if temp > score:
                score = temp
                choices = [i]
            elif score == temp:
                choices.append(i)
    if choices != None:
        return choice(choices)

def minimax(depth: int, board: Board, player: str, maximiser: bool, column: int) -> int:
    board = deepcopy(board)
    #put token in column and check if it can be put in column
    if not board.put_in_column(player, column):
        return
    #return heuristic
    elif depth <= 0:
        return 0
    elif board.check_winner("1"):
        return -depth
    elif board.check_winner("2"):
        return depth
    elif board.is_full():
        return 0
    #return minimum score if not maximiser
    elif not maximiser:
        best = -depth + 1
        score = 1000
        for i in range(1, board.columns+1):
            if board.board[-1][i-1] == "0":
                score = min(score, minimax(depth-1, board, str(3-int(player)), True, i))
                if score == best:
                    break
    #return maximum score if maximiser
    else:
        best = depth-1
        score = -1000
        for i in range(1, board.columns+1):
            if board.board[-1][i-1] == "0":
                score = max(score, minimax(depth-1, board, str(3-int(player)), False, i))
                if score == best:
                    break
    return score
