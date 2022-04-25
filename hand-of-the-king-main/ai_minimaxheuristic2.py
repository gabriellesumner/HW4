'''Minimax with pruning, depth-limited, and heuristic AI
Uses simple minimax structure with alpha/beta pruning to determine AI moves
Utility is based off of the heuristic which evaluates based on banners permanently owned
or percentage of the majority for card types
Isaac Garay and Gabrielle Sumner
'''


from hand_of_the_king import getvalidmoves
import pdb
import random
import math
from copy import deepcopy
import time


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
    start = time.time()
    value = minvalue(board, cards, banners, turn, best, 1 - player, alpha, beta, start)
    for move in moves[1:]:
        v = minvalue(board, cards, banners, turn, move, 1 - player, alpha, beta, start)
        if v > value:
            best = move
            value = v
    return best


def minvalue(board, cards, banners, turn, move, player, alpha, beta, start):
    '''Returns the minimum utility available from a player taking an action on the current board.'''
    # Simulate the action of the current player
    #state = board.copy()
    new_board = deepcopy(board)
    new_cards = deepcopy(cards)
    new_banners = deepcopy(banners)
    sim_move(new_board, move, new_cards, player, new_banners)

    # Check if we are in a terminal state
    moves = getvalidmoves(new_board)
    if len(moves) == 0 or time.time() - start > 30: # if there are no moves left...
        print(f"time difference is {time.time() - start}")
        utility(new_cards, new_banners, player)

    # If not, find minimum utility of possible actions
    value = math.inf
    for move in moves:
        value = min(value, maxvalue(new_board, new_cards, new_banners, turn, move, 1-player, alpha, beta, start))
        if value <= alpha:
            return value
        beta = min(beta, value)
    #board[move] = 0
    # REVERSE MOVES
    return value



def maxvalue(board, cards, banners, turn, move, player, alpha, beta, start):
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
    if len(moves) == 0 or time.time() - start > 30: # if there are no moves left...
        utility(new_cards, new_banners, player)

    # If not, find maximum utility of possible actions
    value = -math.inf
    for move in moves:
        value = max(value, minvalue(new_board, new_cards, new_banners, turn, move, 1 - player, alpha, beta, start))
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

# Calculates the utility at a specific state
# Cards is the list of cards each player owns
# Banners is the list of banners each player has
# Turn shows which player is currently playing
def utility(cards, banners, turn):
    h = 0
    
    #Running through each card collection
    for i in range(len(cards[turn])):
        # Getting the values of:
        #  - How many cards you have of this type
        #  - How many cards your opponent has of this type
        #  - How many cards you need to have a secured banner
        yours = cards[turn][i]
        opponent = cards[1-turn][i]
        majority = (1+2)//2 + 1

        # If the # of cards you and your opponents have are the same
        if yours == opponent:
            # Checking to see if all the cards have been collected
            if yours + opponent == i + 2:
                if banners[turn][i] == 1:
                    h += 1
                # elif banners[1 - turn] == 1:
                #     h -= 1
            # If you are tied and not all the cards have been collected,
            # Check to see you was the last one to pick up a card and get the banner
            else:
                if banners[turn][i] == 1:
                    h += yours/majority
                # elif banners[1 - turn][i] == 1:
                #     h -= opponent/majority

        # Checks to see who has the either the majority or who has the most cards currently
        elif yours >= majority:
            h += 1
        # elif opponent >= majority:
        #     h -= 1
        elif yours > opponent:
            h += yours/majority
        # elif opponent > yours:
        #     h -= opponent/majority
        else:
            print("None of the conditionals were met when defining the utility")
    
    # Return the final heuristic value or the utility of this state
    return h