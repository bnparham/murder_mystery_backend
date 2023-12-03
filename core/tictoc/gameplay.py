from .ai import *

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