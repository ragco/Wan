def is_safe(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n, solution_count):
    if row == n:
        # Print the solution
        print(f"Solution {solution_count[0]}:")
        for r in board:
            print(" ".join("Q" if x == 1 else "." for x in r))
        print()
        solution_count[0] += 1  # Increment the solution count
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solution_count)
            board[row][col] = 0  # Backtrack

def n_queens_solution_count_and_print(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solution_count = [1]  # List used to keep a reference
    solve_n_queens(board, 0, n, solution_count)
    print(f"Total number of solutions: {solution_count[0] - 1}")

# Driver
n = int(input("Enter value of N: "))
n_queens_solution_count_and_print(n)