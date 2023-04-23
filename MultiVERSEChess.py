from Render import *
from Rereader import *

def Main():

    Size = initStart()

    root, canvas, L = initWindow(Size)
    
    All = Loader()

    screenInfo, board_buttons = DrawBoard(root, Size, L)
    DrawPieces(root, All, screenInfo, board_buttons)

    root.mainloop()

    return 

Main()