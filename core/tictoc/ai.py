"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == X:
                x_count += 1
            elif board[row][col] == O:
                o_count += 1
            else:
                continue
    if x_count == 0 and o_count == 0 : return X
    elif x_count > o_count : return O
    elif x_count == o_count : return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = set()
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == EMPTY:
                res.add((row,col))
    return res


def result(board, action):
    x,y = action
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if type(action) is not tuple :
        raise Exception('type is not correct')
    if x not in range(0,3) or y not in range(0,3):
        raise Exception('range is not correct')

    copy_board = copy.deepcopy(board)
    turn = player(board)
    if turn == X : 
        copy_board[x][y] = X
    else :
        copy_board[x][y] = O

    return copy_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """    
    index = 0
    vertial_board = []
    while index < 3 :
        li = []
        for i in range(3):
            li.append(board[i][index])
        vertial_board.append(li)
        index += 1

    # check horizental
    for row in board:
        check = [True for i in row if i == row[0]]
        if len(check) < len(row) : continue
        else :
            # if X win
            if row[0] == X :
                return X
            # if O win
            elif row[0] == O :
                return O

    # check vertical
    for row in vertial_board:
        check = [True for i in row if i == row[0]]
        if len(check) < len(row) : continue
        else :
            # if X win
            if row[0] == X :
                return X
            # if O win
            elif row[0] == O :
                return O
            
    # check dim
    a = board[0][0] if not None else None
    b = board[1][1] if not None else None
    c = board[2][2] if not None else None
    d = board[0][2] if not None else None
    e = board[2][0] if not None else None

    if (a == b and b == c) or (d == b and b == e) :
        if b == X : 
            return X
        elif b == O:
            return O

    # game is Tie 
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or len(actions(board)) == 0:
        return True
    else :
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X : return 1 
        elif winner(board) == O : return -1
        else : return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        moves = actions(board)
        ans = []
        # if X turn
        if player(board) == X :
            for action in moves:
                ans.append([min_value(result(board, action)),action])
            return sorted(ans, key=lambda x : x[0], reverse=True)[0][1]
        # if O turn
        elif player(board) == O :
            for action in moves:
                ans.append([max_value(result(board, action)), action])
            return sorted(ans, key=lambda x : x[0])[0][1]

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board) :
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board) :
        v = max(v, min_value(result(board, action)))
    return v