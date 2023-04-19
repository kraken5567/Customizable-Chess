from Render import *
from txtBoardBuilder import *
from SaveFileReader import *
from Rereader import *

def Main(Game, Debug):
    with open("Options.txt","r") as File:
        if Debug == True:
           Logs = open("ChessDebugger.txt","a")
        winSettings = File.readlines()
        win = []
        for x in winSettings:
            x.replace("\n","")
            win.append(x)
        winHeight=int(win[0])
        winWidth=int(win[1])
            
        Logs.write("\n--New Entry--\n")
        Size = Boarder()
        Logs.write("Board Size: "+str(Size)+"\n")

        global All
        All = Loader()
        Logs.write("Original Board Info(Globalized): "+str(All)+"\n")

        global Clicked
        Clicked = False
        Logs.write("Clicked (Globalized):\n")

        Screen = [0, 0, False]
        Logs.write("Screen ([0,0,F] by default, but will be overriden): "+str(Screen)+"\n")

        global Change
        Change = True

        loopCount = 0
        while Game == True:
            Game = Draw(Size,winWidth,winHeight,All,Screen,Change)
            Logs.write("Curent Game State: "+str(Game)+"\n")
            #Movement = New
            #Logs.write("'Movement' Var: "+str(Movement)+"\n")
        if Game == False:
            Logs.write("Game has closed"+"\n")
        Logs.close()
    return winWidth, winHeight

if True:
    global Game
    Game = True
    Debug = True
    Main(Game, Debug)