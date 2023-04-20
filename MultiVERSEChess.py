from Render import *
from Rereader import *

def Main(Game):

    Size = initStart()

    root, canvas, L = initWindow(Size)
    
    All = Loader()

    screenInfo, board_buttons = DrawBoard(root, Size, L)
    Game = DrawPieces(root, All, screenInfo, board_buttons)

    root.mainloop()

    return 

global Game
Game = True
Main(Game)