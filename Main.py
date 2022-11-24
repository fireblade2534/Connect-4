class Board:
    def __init__(self,Width,Height):
        self.Width=Width
        self.Height=Height
        self.Board=[]
        for X in range(Width):
            self.Board.append(["" for Y in range(Height)])
    
    def PrintBoard(self):
        for Y in range(self.Height):
            Line=[]
            for X in self.Board:
                Line.append(X[Y])
            print(Line)

    def DropPeice(self,Column):
        for X in self.Board[Column]:
            print()


GameBoard=Board(5,5)
        