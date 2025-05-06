# Function to check if placing a queen at (row, col) is safe
def is_safe(board, row, col):
    # Check all previously placed queens (rows 0 to row-1)
    for i in range(row):
        # Check if another queen is in the same column
        # or on the same diagonal (absolute difference of rows equals absolute difference of columns)
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False  # Not safe to place the queen here
    return True  # Safe to place the queen

# Function to print the chessboard configuration
def print_solution(board, n):
    for i in range(n):  # For each row
        # Create a list for the row: 'Q' where the queen is placed, '.' elsewhere
        row = ['Q' if board[i] == j else '.' for j in range(n)]
        print(' '.join(row))  # Print the row as a string with spaces
    print()  # Print a blank line after each solution

# Recursive helper function to solve N-Queens
def solve_n_queens_util(board, row, n, solutions):
    # Base case: if all queens are placed (row == n), we found a solution
    if row == n:
        solutions.append(board[:])  # Add a copy of the current board configuration to solutions
        return  # Backtrack

    # Try placing a queen in every column of the current row
    for col in range(n):
        if is_safe(board, row, col):  # Check if placing at (row, col) is safe
            board[row] = col  # Place the queen at (row, col)
            solve_n_queens_util(board, row + 1, n, solutions)  # Recur to place queen in the next row
            board[row] = -1  # Remove the queen (backtrack) to try next column

# Main function to solve the N-Queens problem
def solve_n_queens(n):
    board = [-1] * n  # Initialize the board: -1 indicates no queen placed in a row
    solutions = []  # List to store all possible solutions
    solve_n_queens_util(board, 0, n, solutions)  # Start solving from row 0

    print(f"\nTotal solutions for {n}-Queens: {len(solutions)}\n")  # Print total number of solutions
    for sol in solutions:  # Print each solution
        print_solution(sol, n)

# 🖊️ Take input from the user
try:
    n = int(input("Enter the value of N (number of queens): "))  # Read integer input
    if n < 1:  # Validate input
        print("Please enter a positive integer greater than 0.")
    else:
        solve_n_queens(n)  # Solve the N-Queens problem
except ValueError:
    print("Invalid input. Please enter an integer.")  # Handle non-integer input
