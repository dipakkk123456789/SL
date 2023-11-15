def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solution(board):
    print("-----------")
    for row in range(len(board)):
        line = ""
        for col in range(len(board)):
            line += " Q " if board[row] == col else " - "
        print(line)
    print("-----------\n")

def solve_n_queens_util(board, row):
    if row == len(board):
        print_solution(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens_util(board, row + 1)

def solve_n_queens(n):
    board = [-1] * n
    solve_n_queens_util(board, 0)

# Solve the 4x4 N-Queens problem
solve_n_queens(4)
