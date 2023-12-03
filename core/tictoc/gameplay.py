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
    action = action if letter == player(board) else minimax(board)
    return(
        {
        'board' : f'{result(board=board,action=action)}',
        'player' : player(board),
        'action' : f"{action}",
        'winner' : winner(board),
        'terminal' : terminal(board),
        }
    )