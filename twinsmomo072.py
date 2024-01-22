import numpy as np
from typing import List, Union

BLACK = -1  # 黒
WHITE = 1   # 白
EMPTY = 0   # 空

class OchibiAI(OthelloAI):
    def __init__(self, face, name):
        self.face = face
        self.name = name

    def move(self, board: np.array, piece: int)->tuple[int, int]:
        valid_moves = get_valid_moves(board, piece)
        return valid_moves[0]

class twinsmomoAI:
    def __init__(self, face, name, depth=3):
        self.face = face
        self.name = name
        self.depth = depth
        self.weights = {'stone_count': 1.0, 'mobility': 1.0, 'corner_bonus': 1.0, 'flipping_potential': 1.0}
    
    def move(self, board: np.array, piece: int) -> tuple[int, int]:
        _, move = self.minimax(board, piece, self.depth)
        return move

    def minimax(self, board, piece, depth):
        if depth == 0 or len(get_valid_moves(board, piece)) == 0:
            return self.evaluate_board(board, piece), None

        valid_moves = get_valid_moves(board, piece)
        if piece == BLACK:  # Maximize for Black
            best_score = float('-inf')
            best_move = None
            for move in valid_moves:
                new_board = board.copy()
                new_board[move[0], move[1]] = piece
                score, _ = self.minimax(new_board, -piece, depth - 1)
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move
        else:  # Minimize for White
            best_score = float('inf')
            best_move = None
            for move in valid_moves:
                new_board = board.copy()
                new_board[move[0], move[1]] = piece
                score, _ = self.minimax(new_board, -piece, depth - 1)
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move

    def evaluate_board(self, board, piece):
        stone_count = count_board(board, piece)
        mobility = len(get_valid_moves(board, piece))
        corner_bonus = self.get_corner_bonus(board, piece)
        flipping_potential = self.get_flipping_potential(board, piece)
        
        # Apply weights to each component
        weighted_sum = (
            self.weights['stone_count'] * stone_count +
            self.weights['mobility'] * mobility +
            self.weights['corner_bonus'] * corner_bonus +
            self.weights['flipping_potential'] * flipping_potential
        )

        return weighted_sum

    def get_corner_bonus(self, board, piece):
        corner_bonus = 0
        N = len(board)
        corners = [(0, 0), (0, N-1), (N-1, 0), (N-1, N-1)]
        for corner in corners:
            if board[corner[0], corner[1]] == piece:
                corner_bonus += 1
        return corner_bonus

    def get_flipping_potential(self, board, piece):
        potential = 0
        for move in get_valid_moves(board, piece):
            potential += len(flip_stones(board, move[0], move[1], piece))
        return potential


def get_valid_moves(board, player):
    return [(r, c) for r, c in all_positions(board) if is_valid_move(board, r, c, player)]

def flip_stones(board, row, col, player):
    N = len(board)
    stones_to_flip = []
    for dr, dc in directions:
        directional_stones_to_flip = []
        r, c = row + dr, col + dc
        while 0 <= r < N and 0 <= c < N and board[r, c] == -player:
            directional_stones_to_flip.append((r, c))
            r, c = r + dr, c + dc
        if 0 <= r < N and 0 <= c < N and board[r, c] == player:
            stones_to_flip.extend(directional_stones_to_flip)
    return stones_to_flip

# プレイヤーの定義
player1 = twinsmomoAI(BLACK, "Player1")
player2 = OchibiAI(WHITE, "OchibiAI")

# ゲームの実行
game(player1, player2, N=8)
