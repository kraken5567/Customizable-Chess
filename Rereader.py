import re

#get file Dialog to save files to a chosen or forced location (export/localsave)

def LineFormatConverter():
    with open("ChessSave.txt", "r") as file:
        n = 0
        Save = file.read()
        rows = Save.splitlines()
        indexer = []
        for a, row in enumerate(rows):
            singleRow = row.replace("|","")
            singleRow = list(singleRow)
            for b, letter in enumerate(singleRow):
                if re.match("[A-Z]", letter) != None:
                    Section = rows[len(rows)-1]
                    Section = Section.replace("[',]","")
                    color = Section[n]
                    indexer.append([a+1, b+1, letter, color])
                    n += 1

def BoxConverter():
    with open("ChessSave.txt", "r") as Lined:
        Lists = Lined.read()
        print(Lists)

def Setter(board,All,row,column):
    for x in All:
        if x[0] == row and x[1] == column:
            board[row-1][column-1] = x[3]
    return board

import json

def Loader():
    with open("ChessSave.json", "r") as file:
        Save = json.load(file)
        rows = Save["Board"]
        All = []
        
    return All


def readSize():
    with open("ChessSave.json", "r") as file:
        Save = json.load(file)
        board = Save["Board"]

        rows = len(Save["Board"])

        Bool = False
        if any(board[0]["Row1"][x] in "0123456789" for x in range(len(board[0]["Row1"]))):
            Bool = True

        if Bool: #== True
            list = []
            for character in range(len(board[0]["Row1"])):
                list.append(board[0]["Row1"][character])
                if any(board[0]["Row1"][character] in range(10)):
                    for Len in range(int(board[0]["Row1"][character])):
                        list.append(Len)
            columns = len(list)
        elif Bool == False:
            columns = len(board[0]["Row1"])

        Size = [rows, columns]
    return Size

def Boarder(Bool,Rows,Columns):
    if Bool: # == True
        tFile = open(r"ChessSave.json", "w")
        Size = [Rows,Columns]
        Board = []

        for rowNum in range(len(Rows)+1,1):
            name = f"Row{rowNum}"
            Board.append({f"{name}":"8"})
        file = {"Board":Board, "turn":"w", "White Castle":"KQ", "Black Castle":"kq"}        

    if Bool == False:
        Size = readSize()
    return Size