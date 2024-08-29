#!/usr/bin/python3

import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the right diagonal
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens_util(board, row, n, solutions):
    """Utility function to solve the N-Queens problem."""
    if row == n:
        # Collect the solution
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens_util(board, row + 1, n, solutions)

            # Backtrack: Remove the queen
            board[row][col] = 0


def solve_nqueens(n):
    """Solve the N-Queens problem."""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions


def main():
    """Main function to parse arguments and solve the N-Queens problem."""
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
