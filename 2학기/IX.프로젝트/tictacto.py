class TicTacToe:
    def __init__(self):
        self.board = [".", ".", ".",\
                      ".", ".", ".",\
                      ".", ".", "."]
        self.current_turn = "X"

    def set(self, row, col):
        # if(self.current_turn == "O") :
        #     self.current_turn = "X"
        # else :
        #     self.current_turn = "O"
        if self.get(row, col) == "." :
            self.current_turn = "X" if self.current_turn == "O" else "O"
            # O면 X를 넣고 아니면 O를 넣어라... 위에 주석 친 if문과 같은 뜻인데 특이한 방법임.

            self.board[(row * 3) + col] = self.current_turn

    def get(self, row, col):
        return self.board[(row * 3) + col]

    def check_winner(self):
        check = self.current_turn

        for i in range(3) :
            if self.get(i, 0) == self.get(i, 1) == self.get(i,2) == check :
                #가로로 빙고가 나왔을 때
                return check
            if self.get(0, i) == self.get(1, i) == self.get(2, i) == check :
                #세로로 빙고가 나왔을 때
                return check

        if self.get(0, 0) == self.get(1, 1) == self.get(2, 2) == check:
            # 대각선으로 빙고가 나왔을 떄
            return check
        elif self.get(0, 2) == self.get(1, 1) == self.get(2, 0) == check:
            # 대각선으로 빙고가 나왔을 떄
            return check
        if not "." in self.board:
            return "d" #무승부다.

    def __str__(self):
        s = ""
        for i, v in enumerate(self.board) :
            s += str(v)
            if i % 3 == 2 :
                s += "\n"
        return s