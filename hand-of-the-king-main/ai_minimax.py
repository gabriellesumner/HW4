from hand_of_the_king import getvalidmoves
import pdb
import random


def get_computer_move(board, cards, banners, turn):
    '''Randomly select a move from the set of valid moves.'''
    moves = getvalidmoves(board)
    return random.choice(moves)