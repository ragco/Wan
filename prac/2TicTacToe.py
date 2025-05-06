import heapq

class TicTacToe:
    def __init__(self, board, player):
        self.board = board
        self.player = player

    def is_winner(self, player):
        # Check all rows, columns, and diagonals for a win
        lines = self.board + list(zip(*self.board))  # rows and columns
        lines.append([self.board[i][i] for i in range(3)])  # diagonal
        lines.append([self.board[i][2 - i] for i in range(3)])  # anti-diagonal
        return any(all(cell == player for cell in line) for line in lines)

    def available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']

    def next_state(self, i, j):
        # Generate the next state after placing a move at (i, j)
        new_board = [row[:] for row in self.board]
        new_board[i][j] = self.player
        next_player = 'O' if self.player == 'X' else 'X'
        return TicTacToe(new_board, next_player)

    def heuristic(self):
        opponent = 'O' if self.player == 'X' else 'X'
        score = 0
        # Check lines for potential winning or blocking opportunities
        for line in self.board + list(zip(*self.board)) + [[self.board[i][i] for i in range(3)]] + [[self.board[i][2-i] for i in range(3)]]:
            if line.count(self.player) == 2 and line.count(' ') == 1:
                score += 10  # Potential winning move
            if line.count(opponent) == 2 and line.count(' ') == 1:
                score -= 8  # Block opponent's winning move
            if line.count(self.player) == 1 and line.count(' ') == 2:
                score += 1 # Block opponent's winning move
        return score

    def __str__(self):
        return '\n'.join([' | '.join(row) for row in self.board])
    
    def __lt__(self, other):
        return str(self.board) < str(other.board)

def a_star_search(game):
    heap = []
    heapq.heappush(heap, (0, game))  # Start with an initial state
    visited = set()

    while heap:
        _, current = heapq.heappop(heap)

        # If current state is a winning state for the player, return it
        if current.is_winner(current.player):
            print("\nWinning Move Found:\n")
            print(current)
            return

        # Avoid revisiting the same state
        board_str = str(current)
        if board_str in visited:
            continue
        visited.add(board_str)

        # Explore all available moves and add them to the heap
        for i, j in current.available_moves():
            next_game = current.next_state(i, j)
            f_score = 1 + next_game.heuristic()  # f = cost + heuristic
            heapq.heappush(heap, (f_score, next_game))

    print("\nNo winning move found.")

# Input functions
def get_board_input():
    print("Enter the board (use X, O, and - for empty):")
    board = []
    for _ in range(3):
        while True:
            row = input().upper().strip().split()
            if len(row) == 3 and all(cell in ['X', 'O', '-'] for cell in row):
                board.append([' ' if c == '-' else c for c in row])
                break
            else:
                print("Enter exactly 3 symbols: X, O, or -")
    return board

def get_starting_player():
    while True:
        p = input("Enter starting player (X/O): ").strip().upper()
        if p in ['X', 'O']:
            return p
        print("Invalid input. Enter X or O.")

# Run program
user_board = get_board_input()
user_player = get_starting_player()
game = TicTacToe(user_board, user_player)
a_star_search(game)
