
def AllSame(List):
    return len(list(set(List))) == 1

def ClearTerminal():
    for X in range(0,300):
        print("  ")

def GetValidResponse(Question,Type=str,Max="None",Min="None"):
    if Max == "None":
        Max=10 ** 20
    if Min == "None":
        Min=-(10 ** 20)
    while True:

        Input=input(Question)
        try:
            Input=Type(Input)
            if Type == int or Type == float:
                if Input >= Min and Input <= Max:
                    return Input
                else:
                    print(f"Please enter a number within {Min} and {Max}" )
            else:
                return Input
        except:
            print(f"Please enter a value of type {Type.__name__}")
        
class Board:
    def __init__(self,Width,Height,WinNumber=4):
        self.Width=Width
        self.Height=Height
        self.Board=[]
        self.WinNumber=WinNumber
        for X in range(Width):
            self.Board.append(["  " for Y in range(Height)])
    
    def PrintBoard(self):
        for Y in range(self.Height):
            Line=[]
            for X in self.Board:
                Line.append(X[Y])
            print("|{0}|".format("|".join(Line)))

    def DropPeice(self,Column,Peice):
        for X,Y in enumerate(self.Board[Column]):
            if self.Board[Column][self.Height - X - 1] == "  ":
                self.Board[Column][self.Height - X - 1]=Peice
                return True
        return False


    def CheckDiagonals(self):
        CounterX=0
        while CounterX <= self.Width - self.WinNumber or CounterX == 0:
            
            CounterY=0
            while CounterY <= self.Height - self.WinNumber or CounterY == 0:
                #print(CounterX,CounterY)
                
                ListRD=[]
                for A in range(0,self.WinNumber):
                    #print(CounterX + A, CounterY + A,"R")
                    ListRD.append(self.Board[CounterX + A][CounterY + A])
               


                ListLD=[]
                for A in range(0,self.WinNumber):
                    #print(CounterX + A, len(self.Board[CounterX]) - (CounterY + A) - 1,"L")
                    ListLD.append(self.Board[CounterX + A][self.Height - (CounterY + A) - 1])


                if AllSame(ListLD) and ListLD[0] != "  ":
                    return [True,ListLD[0]]
                if AllSame(ListRD) and ListRD[0] != "  ":
                    return [True,ListRD[0]]
                
                #print(ListLD,ListRD)
                CounterY+=1
            CounterX+=1
        return [False]
    def CheckRow(self):
        CounterX=0
        while CounterX <= self.Width - self.WinNumber or CounterX == 0:
            for Y in range(self.Height):
                List=[]
                for A in range(self.WinNumber):
                    List.append(self.Board[CounterX + A][Y])
                #print(List)
                if AllSame(List) and List[0] != "  ":
                    return [True,List[0]]
            CounterX+=1
        return [False]

    def CheckCol(self):
        CounterY=0
        while CounterY <= self.Height - self.WinNumber or CounterY == 0:
            for X in range(self.Width):
                List=[]
                for A in range(self.WinNumber):
                    List.append(self.Board[X][CounterY + A])
                #print(List)
                if AllSame(List) and List[0] != "  ":
                    return [True,List[0]]
            CounterY+=1
        return [False]

    def IsFull(self):
        for X in self.Board:
            for Y in X:
                if Y == "  ":
                    return False
        return True
    
def RunGame():
    Width=7
    Height=6

    GameBoard=Board(Width,Height)
    Move="🟡"
    ClearTerminal()
    GameBoard.PrintBoard()
    while True:
        
        Input=GetValidResponse(f"{Move} Move (Column): ",Type=int,Max=Width,Min=1)

        if GameBoard.DropPeice(Input - 1,Move) == False:
            print("Column {Input} is full")
        else:
            
                
            ClearTerminal()
            if Move == "🔴":
                Move="🟡"
            else:
                Move="🔴"
            GameBoard.PrintBoard()
            Dia=GameBoard.CheckDiagonals()
            Row=GameBoard.CheckRow()
            Col=GameBoard.CheckCol()
            Winner=""
            if Dia[0]:
                Winner=Dia[1]
            elif Row[0]:
                Winner=Row[1]
            elif Col[0]:
                Winner=Col[1]
            
            GameEnd=False
            if Winner != "":
                print(f"{Winner} has won!")
                GameEnd=True
            if GameBoard.IsFull():
                print("Draw!")
                GameEnd=True
            if GameEnd:
                Input=input("Again (Y/N): ")
                if Input.lower() == "y":
                    return
                else:
                    exit()

while True:
    RunGame()