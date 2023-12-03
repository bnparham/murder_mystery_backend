from .ai import *
import ast

def startNewGame_method():
    return(
        {
            'board' : f'{initial_state()}',
            'player' : 'X',
            'action' : None,
            'winner' : None,
            'terminal' : False,
            'move' : None,
        }
    )

def PlayerMove(board,action,letter):
    board = ast.literal_eval(board)
    action = tuple(action) if letter == player(board) else minimax(board)
    res = result(board=board,action=action)
    return(
        {
        'board' : f'{res}',
        'player' : player(board),
        'action' : f"{action}",
        'winner' : winner(res),
        'terminal' : terminal(res),
        }
    )