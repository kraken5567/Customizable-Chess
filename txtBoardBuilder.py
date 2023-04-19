from SaveFileReader import *
#Remove "All" Reliance 
#def ColorString(All):
#    color = []
#   DFile = open(r"ChessDebugger.txt", "w")
#    for f in range(len(All)):
#        ind = All[f]
#        DFile.write("List Var:"+str(ind)+'\n')
#        color += ind[2]
#        DFile.write("Color Var:"+str(color)+'\n')
#    return color

#remove "All" Functionallity
def Setter(board,All,row,column):
    for x in All:
        if x[0] == row and x[1] == column:
            board[row-1][column-1] = x[3]
    return board

def Boarder():
    NewOrOld = input("Create or Load Board? (c/l): ")
    if NewOrOld == "c":
        #Creation of File Works
        tFile = open(r"ChessSave.txt", "w")
        Size = []
        Row = int(input("Number of Rows: ")) #Size[0] = Row
        Column = int(input("Number of Columns: ")) #Size[1] = Column
        Size.append(Row)
        Size.append(Column)
        board = [[str(i) for i in range(1, Column + 1)] for _ in range(Row)]
        for row in board:
            tFile.write("|" + "|".join(list(row)) + "|")
            tFile.write("\n")
        tFile.write("wb")
    if NewOrOld == "l":
        Size = readSize()
    return Size