'''Minimax with pruning AI
Uses simple minimax structure with alpha/beta pruning to determine AI moves
Utility is based off of winning or losing the final game
Isaac Garay and Gabrielle Sumner
'''

from hand_of_the_king import getvalidmoves
import pdb
import random
import math
from copy import deepcopy


def get_computer_move(board, cards, banners, turn):
    '''Randomly select a move from the set of valid moves.'''
    player = turn
    return minimax(board, cards, banners, turn, player)


def minimax(board, cards, banners, turn, player):
    '''Returns the best action from a given state in the game for a specific player.'''
    moves = getvalidmoves(board)
    best = moves[0]
    alpha = -math.inf
    beta = math.inf
    value = minvalue(board, cards, banners, turn, best, 1 - player, alpha, beta)
    for move in moves[1:]:
        v = minvalue(board, cards, banners, turn, move, 1 - player, alpha, beta)
        if v > value:
            best = move
            value = v
    return best


def minvalue(board, cards, banners, turn, move, player, alpha, beta):
    '''Returns the minimum utility available from a player taking an action on the current board.'''
    # Simulate the action of the current player
    #state = board.copy()
    new_board = deepcopy(board)
    new_cards = deepcopy(cards)
    new_banners = deepcopy(banners)
    sim_move(new_board, move, new_cards, player, new_banners)

    # Check if we are in a terminal state
    moves = getvalidmoves(new_board)
    if len(moves) == 0: # if there are no moves left...
        # board[move] = 0 # 
        # REVERSE whatever move was taken

        # if AI has more banners, return 1
        if sum(new_banners[turn]) > sum(new_banners[1-turn]):
            return 1
        # if other player has more banners, return -1
        elif sum(new_banners[1-turn]) > sum(new_banners[turn]):
            return -1
        else: # else tie, return 0
            return 0

    # If not, find minimum utility of possible actions
    value = math.inf
    for move in moves:
        value = min(value, maxvalue(new_board, new_cards, new_banners, turn, move, 1-player, alpha, beta))
        if value <= alpha:
            return value
        beta = min(beta, value)
    #board[move] = 0
    # REVERSE MOVES
    return value



def maxvalue(board, cards, banners, turn, move, player, alpha, beta):
    '''Returns the maximum utility available from a player taking an action on the current board.'''
    # Simulate the action of the current player
    #state = board.copy()
    # simulate
    new_board = deepcopy(board)
    new_cards = deepcopy(cards)
    new_banners = deepcopy(banners)
    sim_move(new_board, move, new_cards, player, new_banners)

    # Check if we are in a terminal state
    moves = getvalidmoves(new_board)
    if len(moves) == 0: # if there are no moves left...
        # board[move] = 0 # 
        # REVERSE whatever move was taken

        # if AI has more banners, return 1
        if sum(new_banners[turn]) > sum(new_banners[1-turn]):
            return 1
        # if other player has more banners, return -1
        elif sum(new_banners[1-turn]) > sum(new_banners[turn]):
            return -1
        else: # else tie, return 0
            return 0

    # If not, find maximum utility of possible actions
    value = -math.inf
    for move in moves:
        value = max(value, minvalue(new_board, new_cards, new_banners, turn, move, 1 - player, alpha, beta))
        if value <= alpha:
            return value
        beta = max(beta, value)
    #board[move] = 0
    # REVERSE MOVES
    return value


def sim_move(board, x, collection, turn, banners):
    '''Move the 1-card in the GUI to the position on the board specified by the input index, capturing
    cards of the same color along the way. Update the player's card collection accordingly.
    
    Note that x0 is the intial position of the 1-card in the objects array, which we need to correctly move it around.'''
    # Get relevant data
    x1 = board.index(1)  # index of the 1-card on the board
    # print(f'moving from {x1} to {x}')

    # Remove captured cards from board
    color = board[x]  # color of the main captured card
    board[x] = 1  # the 1-card moves here
    collection[turn][color - 2] += 1
    if abs(x - x1) < 6:  # move is either left or right
        if x < x1:  # left
            possible = range(x + 1, x1)
        else:  # right
            possible = range(x1 + 1, x)
    else:  # move is either up or down
        if x < x1:  # up
            possible = range(x + 6, x1, 6)
        else:  # down
            possible = range(x1 + 6, x, 6)

    for i in possible:
        if board[i] == color:
            board[i] = 0  # there is no card in this position anymore

    # Move the 1-card to the correct position
    collection[turn][color - 2] += 1
    board[x1] = 0

    if collection[turn][color - 2] >= collection[abs(turn - 1)][color - 2]:
        banners[turn][color - 2] = 1  # add the banner to the player's collection
        banners[abs(turn - 1)][color - 2] = 0
    
    return