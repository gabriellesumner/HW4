from hand_of_the_king import getvalidmoves
import pdb
import random
import math


def get_computer_move(board, cards, banners, turn):
    '''Randomly select a move from the set of valid moves.'''
    moves = getvalidmoves(board)
    return random.choice(moves)


def minimax(board, player):
    '''Returns the best action from a given state in the game for a specific player.'''
    actions = getvalidmoves(board, player)
    best = actions[0]
    # alpha = -math.inf
    # beta = math.inf
    value = minvalue(board, player, best)
    for action in actions[1:]:
        v = minvalue(board, player, action)
        if v > value:
            best = action
            value = v
    return best


def minvalue(board, player, action):
    '''Returns the minimum utility available from a player taking an action on the current board.'''
    # Simulate the action of the current player
    #state = board.copy()
    board[action[0], action[1]] = player
    nextplayer = 3 - player

    # Check if we are in a terminal state
    moves = getvalidmoves(board, nextplayer)
    if len(moves) == 0:
        board[action[0], action[1]] = 0
        return 1

    # If not, find minimum utility of possible actions
    value = math.inf
    for move in moves:
        value = min(value, maxvalue(board, nextplayer, move))
        # if value <= alpha:
        #     board[action[0], action[1]] = 0
        #     return value
    board[action[0], action[1]] = 0
    return value



def maxvalue(board, player, action):
    '''Returns the maximum utility available from a player taking an action on the current board.'''
    # Simulate the action of the current player
    #state = board.copy()
    board[action[0], action[1]] = player
    nextplayer = 3 - player

    # Check if we are in a terminal state
    moves = getvalidmoves(board, nextplayer)
    if len(moves) == 0:
        board[action[0], action[1]] = 0
        return -1

    # If not, find maximum utility of possible actions
    value = -math.inf
    for move in moves:
        value = max(value, minvalue(board, nextplayer, move))
        # if value >= beta:
        #     board[action[0], action[1]] = 0
        #     return value
    board[action[0], action[1]] = 0
    return value