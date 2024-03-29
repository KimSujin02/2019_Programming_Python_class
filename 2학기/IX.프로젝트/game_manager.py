from tictacto import TicTacToe
import tkinter
from tictacto import messagebox

class Game_Manager:
    def __init__(self):
        self.ttt = TicTacToe()

    def play(self):
        #게임판 보여주자
        print(self.ttt)
        while True :
            #row, col 입력받자
            row = int(input("row : "))
            col = int(input("col : "))
            self.ttt.set(row, col)
            print(self.ttt)
            #check_winner 면 끝내자
            if self.ttt.check_winner() == "0":
                print("O win!")
                break
            elif self.ttt.check_winner() == "X":
                print("X win!")
                break
            elif self.ttt.check_winner() == "d":
                print("무승부!")
                break

class GameManager_GUI:
    def __init__(self):
        self.ttt = TicTacToe()
        CANVAS_SIZE = 300
        self.TILE_SIZE = CANVAS_SIZE / 3

        self.root = tkinter.Tk()
        self.root.title("틱택토")
        self.root.geometry(str(CANVAS_SIZE)+"x"+str(CANVAS_SIZE))
        self.root.resizable(width=False, height=False)
        self.canvas = tkinter.Canvas(self.root, bg="white", width=CANVAS_SIZE, height=CANVAS_SIZE)
        self.canvas.pack()

        self.images = dict()
        self.images["O"] = tkinter.PhotoImage(file="img/O.gif")
        self.images["X"] = tkinter.PhotoImage(file="img/X.gif")

        self.canvas.bind("<Button-1>", self.click_handler)

    def click_handler(self, event):
        row = int(event.y//self.TILE_SIZE) #math.floor(event.y/self.TILE_SIZE)
        col = int(event.x//self.TILE_SIZE)
        self.ttt.set(row, col)
        # print(self.ttt)
        #draw_board()
        self.draw_board()
        #check_winner()
        if self.ttt.check_winner() == "O" :
            messagebox.showinfo("게임오버", "O win!")
            self.root.quit()
        if self.ttt.check_winner() == "X" :
            messagebox.showinfo("게임오버", "X win!")
            self.root.quit()
        if self.ttt.check_winner() == "d" :
            messagebox.showinfo("게임오버", "무승부!")
            self.root.quit()

    def draw_board(self):
        self.canvas.delete("all")

        x=0
        y=0

        for i, v in enumerate(self.ttt.board):
            if v == ".":
                pass
            elif v == "O":
                self.canvas.create_image(x, y, anchor="nw", image=self.images["O"])
            elif v == "X":
                self.canvas.create_image(x, y, anchor="nw", image=self.images["X"])
            x += self.TILE_SIZE
            if i % 3 == 2:
                x=0
                y += self.TILE_SIZE

    def play(self):
        self.root.mainloop()

if __name__ == '__main__' :
    gm = GameManager_GUI()
    gm.play()