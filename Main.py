class Board:
    def __init__(self,Width,Height):
        self.Width=Width
        self.Height=Height
        self.Board=[]
        for X in range(Width):
            self.Board.append([" " for Y in range(Height)])
    
    def PrintBoard(self):
        for Y in range(self.Height):
            Line=[]
            for X in self.Board:
                Line.append(X[Y])
            print("|{0}|".format("|".join(Line)))

    def DropPeice(self,Column,Peice):
        for X,Y in enumerate(self.Board[Column]):
            if self.Board[Column][self.Height - X - 1] == " ":
                self.Board[Column][self.Height - X - 1]=Peice
                return True
        return False


GameBoard=Board(5,5)
GameBoard.PrintBoard() 
print("\n\n")
GameBoard.DropPeice(0,"R")
GameBoard.PrintBoard()