class TicTacToe:

    def __init__(self, n: int):
        self._row_cnt = [0] * n
        self._col_cnt = [0] * n
        self._diag_cnt = 0
        self._anti_diag_cnt = 0
        self._size = n
        """
        0, 0  0, 1  0, 2

        1, 0  1, 1  1, 2

        2, 0

        """
        

    def move(self, row: int, col: int, player: int) -> int:
        curr_player_move = 1 if player == 1 else -1
        self._row_cnt[row] += curr_player_move
        self._col_cnt[col] += curr_player_move

        if row == col:
            self._diag_cnt += curr_player_move
        
        if col == (self._size - row - 1):
            self._anti_diag_cnt += curr_player_move


        if (
            abs(self._row_cnt[row]) == self._size or
            abs(self._col_cnt[col]) == self._size or
            abs(self._diag_cnt) == self._size or 
            abs(self._anti_diag_cnt) == self._size
        ):
            return player

        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)