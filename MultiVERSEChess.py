from Render import *
from txtBoardBuilder import *
from SaveFileReader import *
from Rereader import *

def Main(Game):

    with open("Options.txt","r") as File:
        winSettings = File.readlines()
        File.close()
        win = []
        for x in winSettings:
            x.replace("\n","")
            win.append(x)

        winHeight=int(win[0])
        winWidth=int(win[1])
            
        Size = Boarder()
        All = Loader()

        root, canvas, screenInfo, board_buttons = DrawBoard(Size,winWidth,winHeight)
        Game = DrawPieces(root, All, screenInfo, board_buttons)

        while True:
            root.mainloop()

    return winWidth, winHeight

global Game
Game = True
Main(Game)