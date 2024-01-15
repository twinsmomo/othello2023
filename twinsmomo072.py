class SmartOthelloAI(OthelloAI):
    def __init__(self):
        self.face = '🍑'  # 自分の好きな絵文字
        self.name = 'もも'  # 自分の好きな名前

    def move(self, board: np.array, color: int) -> tuple[int, int]:
        # コツ①: 確定石を取られない
        # コツ④: 相手に囲ませる
        best_move = self.prevent_disks_taken(board, color)

        # コツ②: 序盤は少なく取る
        if count_board(board, color) < 8:
            best_move = self.take_fewer_disks(board, color)

        # コツ③: 中盤は開放度理論
        elif 8 <= count_board(board, color) < 30:
            best_move = self.liberty_theory(board, color)

        # コツ⑤: 終盤は偶数理論
        elif count_board(board, EMPTY) <= 8:
            best_move = self.even_discs_theory(board, color)

        return best_move

    def prevent_disks_taken(self, board, color):
        # ここに確定石を取られないためのロジックを実装
        pass

    def take_fewer_disks(self, board, color):
        # ここに序盤は少なく取るためのロジックを実装
        pass

    def liberty_theory(self, board, color):
        # ここに中盤は開放度理論を考慮したロジックを実装
        pass

    def even_discs_theory(self, board, color):
        # ここに終盤は偶数理論を考慮したロジックを実装
        pass

# 新しいAIを作成
smart_ai = SmartOthelloAI()

# ゲームを実行
game(momo, smart_ai, N=8)
