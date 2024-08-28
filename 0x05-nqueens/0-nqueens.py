#!/usr/bin/python3

import sys



def is_valid():

def n_queens(n, row, column):
    '''start solving the nqueens'''

    n_list = []

    if sys.argv != 2:
        print("Usage: nqueens N\n")
        exit(1)

    if type(n) is not int:
        print("N must be a number\n")
        exit(1)
    elif n < 4:
        print("N must be a number\n")
        exit(1)
    else:
        chess_board = []
        chess_board = n * n

        queen = n
        for row in chess_board:
            for column in chess_board:
                chess_board[row][column] = queen
                if chess_board[row][column] == True:
                    n_list.append(chess_board[row][column])
                if chess_board[row = False][column = True]:
                    n_queens(n, row + 1,  column)
         

