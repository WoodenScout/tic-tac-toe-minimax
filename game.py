from board import Board
from tile import Tile


class Game:
    def __init__(self, board):
        self.board = board.board_state


    def check_winner(self):
        for row in range(3):
            if self.board[row][0].piece == self.board[row][1].piece == self.board[row][2].piece:
                return self.board[row][0].piece
        for col in range(3):
            if self.board[0][col].piece == self.board[1][col].piece == self.board[2][col].piece:
                return self.board[0][col].piece
        if self.board[0][0].piece == self.board[1][1].piece == self.board[2][2].piece:
            return self.board[0][0].piece
        if self.board[0][2].piece == self.board[1][1].piece == self.board[2][0].piece:
            return self.board[0][2].piece
        
        flag = False
        for row in range(3):
            for col in range(3):
                if self.board[row][col].piece is not None:
                    continue
                else:
                    flag = True
                    break
        if not flag:
            return 'TIE'

        return None
    

    def get_moves(self):
        moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col].piece is None:
                    moves.append((row, col))
        return moves


    def make_move(self, row:int, col:int, piece:str):
        self.board[row][col].piece = piece


    def evaluate(self):
        if self.check_winner() == 'X':
            return 10
        elif self.check_winner() == 'O':
            return -10
        else:
            return 0


    def minimax(self, player:str = 'X', depth:int = 9):
        if player == 'X':
            best = [-1, -1, -10] # row, col, score
        else:
            best = [-1, -1, 10] # row, col, score
        
        if depth == 0 or self.check_winner() is not None:
            score = [-1, -1, self.evaluate()] # row, col, score
            return score
        
        for move in self.get_moves():
            row, col = move
            self.make_move(row, col, player) # make the move
            score = self.minimax('X' if player == 'O' else 'O', depth - 1)
            self.make_move(row, col, None) # undo the move
            score[0], score[1] = row, col

            if player == 'X':
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score
        
        return best
    
    def alphabeta(self, player:str = 'X', depth:int = 9, alpha:float = float('-inf'), beta:float = float('inf')):
        if player == 'X':
            best = [-1, -1, -10] # row, col, score
        else:
            best = [-1, -1, 10] # row, col, score
        
        if depth == 0 or self.check_winner() is not None:
            score = [-1, -1, self.evaluate()] # row, col, score
            return score
        
        for move in self.get_moves():
            row, col = move
            self.make_move(row, col, player) # make the move
            score = self.minimax('X' if player == 'O' else 'O', depth - 1)
            self.make_move(row, col, None) # undo the move
            score[0], score[1] = row, col

            if player == 'X':
                if score[2] > best[2]:
                    best = score
                if score[2] > beta:
                    break
                alpha = max(alpha, score[2])

            else:
                if score[2] < best[2]:
                    best = score
                if score[2] < alpha:
                    break
                beta = min(beta, score[2])
        
        return best