# nQueens.py : Solve the N-Queens problem
# Aaditya Arigela, September 2017
#
# The N-queens problem is: Given an empty NxN chessboard, place N queens on the board so that no queen
# can attack any other, i.e. such that no two queens share the same row, column or diagonal.

#!/usr/bin/env python3


import sys

# Utility function to print board in human-friendly format
def printable_board():
    for i in range(N):
        for j in range(N):

            # Marked unavailable
            if initial_board[i][j] == -1:
                print("X"),

            # Queen
            elif initial_board[i][j] == 1:
                print("Q"),

            # Empty square
            else:
                print("_"),
        print

def solver(row):
    # This means all queens are placed
    if row == N:
        printable_board()
        exit()

    # Consider this row and try placing a queen in all columns one by one
    for col in range(N):
        if initial_board[row][col] != -1 and occupied_cols[col] == False and occupied_diag1[row - col + N - 1] == False and occupied_diag2[row + col] == False:

            occupied_cols[col] = occupied_diag1[row - col + N - 1] = occupied_diag2[row + col] = True
            initial_board[row][col] = 1;

            solver(row + 1);
            occupied_cols[col] = occupied_diag1[row - col + N - 1] = occupied_diag2[row + col] = False
            initial_board[row][col] = 0;

    # if queen can not be placed anywhere then return false
    return False;

def solveNQueens():
    if solver(0) == False:
        print("Solution does not exist for given 'N'")


# This is N, the size of the board. It is passed through command line arguments.
N = int(sys.argv[1])

# The board is stored as a list-of-lists. Each inner list contains row and column of a queen on the board.
# An empty list indicates no piece, and elements in the list indicates pieces on the board.
initial_board = [[0 for x in range(N)] for y in range(N)]

# Indexes
occupied_cols = [False for i in range(N)]
occupied_diag1 = [False for i in range(2 * N - 1)]
occupied_diag2 = [False for i in range(2 * N - 1)]

# Driver function
solveNQueens();