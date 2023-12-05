from .ai import *
import ast

def startNewGame_method():
    return(
        {
            'board' : f'{compressBoard(initial_state())}',
            'player' : 'X',
            'action' : None,
            'winner' : None,
            'terminal' : False,
            'move' : None,
        }
    )

def PlayerMove(board,action,letter):
    board = extractBoard(board)
    action = extractAction(action) if letter == player(board) else minimax(board)
    res = result(board=board,action=action)
    return(
        {
        'board' : f'{compressBoard(res)}',
        'player' : player(board),
        'action' : f"{compressAction(action)}",
        'winner' : winner(res),
        'terminal' : terminal(res),
        }
    )


def compressBoard(board:list):
    res = ''
    for row in range(len(board)):
        for col in range(len(board)):
            match board[row][col]:
                case None : res += '0'
                case 'X' : res += '1'
                case 'O' : res += '2'
    return res

def extractBoard(board:str):
    mapping = {'0': None, '1': 'X', '2': 'O'}
    
    # Check if the length of the input string is divisible by 3
    if len(board) % 3 != 0:
        raise ValueError("Input string length must be a multiple of 3.")
    
    # Convert the string into a list of lists
    result = [[mapping[board[i]], mapping[board[i + 1]], mapping[board[i + 2]]] for i in range(0, len(board), 3)]
    
    return result


def compressAction(action:tuple):
    res = ''
    for t in action:
        res += f'{t}'
    return res

def extractAction(action:str):
    res = []
    for i in action:
        res.append(int(i))
    return tuple(res)