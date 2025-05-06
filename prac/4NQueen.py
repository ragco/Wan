def is_safe(board, row, col, n):
    # Check column and diagonals
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def print_solution(board, n):
    for i in range(n):
        row = ['Q' if board[i] == j else '.' for j in range(n)]
        print(' '.join(row))
    print()

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row] = -1  # Backtrack

def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    
    print(f"\nTotal solutions for {n}-Queens: {len(solutions)}\n")
    for sol in solutions:
        print_solution(sol, n)

# 🖊️ Take input from the user
try:
    n = int(input("Enter the value of N (number of queens): "))
    if n < 1:
        print("Please enter a positive integer greater than 0.")
    else:
        solve_n_queens(n)
except ValueError:
    print("Invalid input. Please enter an integer.")
