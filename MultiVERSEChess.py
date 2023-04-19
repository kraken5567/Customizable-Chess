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
        Clicked = False
        Screen = [0, 0, False]
        Change = True
        loopCount = 0

        while Game == True:
            Game = Draw(Size,winWidth,winHeight,All,Screen,Change)
    return winWidth, winHeight

if True:
    global Game
    Game = True
    Main(Game)