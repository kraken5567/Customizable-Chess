import json
from tkinter import *
from PIL import ImageTk, Image

from PieceInfoer import *
from Rereader import *
from Movement import Movement

def initStart():
    root = Tk()
    root.title('Multiverse Chess Menu')

    File = open("Options.json","r")
    winSettings = json.load(File)
    File.close()
    winHeight=int(winSettings["xRes"])
    winWidth=int(winSettings["yRes"])

    Res = Label(root,text="Resolution")
    xRes = Entry(root)
    xRes.insert(0,winWidth)
    yRes = Entry(root)
    yRes.insert(0,winHeight)
    
    Row = Entry(root)
    Column = Entry(root)

    global Size
    Size = "None"

    def SizeGetter(Bool,Rows,Columns):
        global Size
        Size = Boarder(Bool,Rows,Columns)

    Load = Button(root, text="Load Save",command = lambda: SizeGetter(False,Row.get(),Column.get()))
    Create = Button(root, text="Create Save",command = lambda: SizeGetter(True,Row.get(),Column.get()))

    Res.grid(row=0,columnspan=2)

    xRes.grid(row=1,column=0)
    yRes.grid(row=1,column=1)

    Row.grid(row=2,column=0)
    Column.grid(row=2,column=1)
    
    Create.grid(row=3,columnspan=2)

    Load.grid(row=4,columnspan=2)

    while Size == "None":
        root.update()

    root.destroy()
    SizeList = Size
    del Size
    return SizeList
        

def initWindow(Size):

    File = open("Options.json","r")
    winSettings = json.load(File)
    
    winHeight=int(winSettings["xRes"])
    winWidth=int(winSettings["yRes"])

    root = Tk()
    root.title('Multiverse Chess Board')
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    if winWidth > winHeight:
        L = winHeight
    elif winHeight > winWidth:
        L = winWidth
    else:
        L = winWidth

    File.close()

    return root, canvas, L

def DrawBoard(root,Size,L):

    yRatio = int(L / Size[0])
    xRatio = int(L / Size[1])

    # Create 2D list of buttons
    board_buttons = []
    for col in range(Size[1]):
        button_row = []
        for row in range(Size[0]):
            image_x = row * L / Size[0]
            image_y = col * L / Size[1]
            if (row + col) % 2 == 0:
                color = "#323232"
            else:
                color = "#CDCDCD"
            button = Button(root, bg=color, activebackground=color, bd=0, command= lambda sqr = [row, col, None, None]: Movement.MovedPiece(sqr, board_buttons))
            button.place(x=image_x, y=image_y, width=xRatio, height=yRatio)
            button_row.append(button)
        board_buttons.append(button_row)

    return [xRatio, yRatio], board_buttons


def DrawPieces(root, All, screenInfo, board_buttons):
    xRatio, yRatio = screenInfo

    for i in range(len(All)):
        l = All[i]
        a = l
        y_val = (a[0])*(yRatio)
        x_val = (a[1])*(xRatio)

        # Load image
        imgName = Image.open("Pieces/"+str(a[3])+str(a[2])+".png")
        imgName = imgName.resize((int(xRatio), int(yRatio)), Image.ANTIALIAS)
        imgName = ImageTk.PhotoImage(imgName)

        # Configure board button with image
        board_button = board_buttons[a[0]][a[1]]
        board_button.config(image=imgName, command= lambda sqr = All[i]: Movement.MovedPiece(sqr, board_buttons))
        board_button.image = imgName  # Keep a reference to prevent garbage collection

    root.update()
        
    return board_buttons