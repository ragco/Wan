import heapq

class ttt:
    def __init__(self, board, playr):
        self.board = board
        self.playr = playr

    def is_win(self , plyr):
        lins = self.board + list(zip(*self.board)) + [self.board[i][i] for i in range (3)] + [self.board[i][2-i] for i in range (3)]
        return any(all(cell == playr for cell in lin)for lin in lins)
    
    def avl_moves(self):
        return [(i,j) for i in range(3) for j in  range (3) if self.board[i][j] == " "]
    
    def nxt_state(self , i , j):
        nbrd = [row[:] for row in self.board]
        nbrd[i][j] = self.playr
        nplyr = 'O' if self.playr == 'X' else 'X'
        return ttt(nbrd , nplyr)
    
    def hurstic(self):
        opp = 'O' if self.playr == 'X' else 'X'
        scr = 0
        for line in self.board + list(zip(*self.board)) + [[self.board[i][i] for i in range(3)]] + [[self.board[i][2-i] for i in range(3)]]:
            if line.count(self.playr) == 2 and line.count(' ') == 1:
                score += 10 
            if line.count(opp) == 2 and line.count(' ') == 1:
                score -= 8
            if line.count(self.player) == 1 and line.count(' ') == 2:
                score += 1
        return score

def a_str(game):
    heap = []
    heapq.heappush(heap, (0,game))
    visted = set()

    while heap:
        _,curnt = heapq.heappop(heap)
        
        if curnt.is_win(curnt.playr):
            print("\nWinning Move Found:\n")
            print(curnt)
            return
        
        board_str = str(curnt)
        if board_str in visted:
            continue
        visted.add(board_str)

        for i,j in curnt.avl_moves():
            nxt = curnt.nxt_state(i,j)
            f_scr = 1 + nxt.hurstic()
            heapq.heappush(heap , (f_scr , nxt))
    print("No winning move found.")

def get_board():
    board = []
    print("Enter the board (3x3) row by row, using 'X', 'O', or ' ' for empty spaces:")
    for i in range(3):
        while(True):
            row = input().upper().strip().split()
            if len(row) == 3 and all(cell in [ 'X' , 'O' , '-' ] for cell in row):
                board.append([' ' if c == '-' else c for c in row])
                break
            else:
                print("enter correct : ")
    return board

def get_playr():
    while True:
        p = input("Enter Starting playr : ").strip().upper()
        if p in ['X', 'O']:
            return p
        print("Invalid input. Enter X or O.")

board = get_board()
playr = get_playr()
game = ttt(board, playr)
a_str(game)