from hand_of_the_king import getvalidmoves
import pdb
import random
import math


def get_computer_move(board, cards, banners, turn):
    '''Randomly select a move from the set of valid moves.'''
    return minimax(board, cards, banners, turn)


def minimax(board, cards, banners, turn):
    '''Returns the best action from a given state in the game for a specific player.'''
    moves = getvalidmoves(board)
    best = moves[0]
    # alpha = -math.inf
    # beta = math.inf
    value = minvalue(board, cards, banners, turn, best)
    for move in moves[1:]:
        v = minvalue(board, cards, banners, turn, move)
        if v > value:
            best = move
            value = v
    return best


def minvalue(board, cards, banners, turn, move):
    '''Returns the minimum utility available from a player taking an action on the current board.'''
    # Simulate the action of the current player
    #state = board.copy()
    sim_move(board, cards, banners, turn, move)

    # Check if we are in a terminal state
    moves = getvalidmoves(board)
    if len(moves) == 0:
        board[move] = 0
        return 1

    # If not, find minimum utility of possible actions
    value = math.inf
    for move in moves:
        value = min(value, maxvalue(board, move))
        # if value <= alpha:
        #     board[action[0], action[1]] = 0
        #     return value
    board[move] = 0
    return value



def maxvalue(board, player, action):
    '''Returns the maximum utility available from a player taking an action on the current board.'''
    # Simulate the action of the current player
    #state = board.copy()
    # simulate

    # Check if we are in a terminal state
    moves = getvalidmoves(board)
    if len(moves) == 0:
        board[move] = 0
        return -1

    # If not, find maximum utility of possible actions
    value = -math.inf
    for move in moves:
        value = max(value, minvalue(board, move))
        # if value >= beta:
        #     board[action[0], action[1]] = 0
        #     return value
    board[move] = 0
    return value


def sim_move(board, cards, banners, turn, move):
    '''Simulate a move'''
    pass