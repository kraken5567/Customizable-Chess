import json
from tkinter import *
from PIL import ImageTk, Image

from PieceInfoer import *
from Rereader import *

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
            button = Button(root, bg=color, activebackground=color, bd=0)
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
        imgName = Image.open("Pieces/"+str(a[3])+str(a[2])+"/"+str(a[3])+str(a[2])+".png")
        imgName = imgName.resize((int(xRatio), int(yRatio)), Image.ANTIALIAS)
        imgName = ImageTk.PhotoImage(imgName)

        # Configure board button with image
        board_button = board_buttons[a[0]][a[1]]
        board_button.config(image=imgName)
        board_button.image = imgName  # Keep a reference to prevent garbage collection

    root.update()
        

def MovedPiece(event, sqr, All):
    try:
        sqr
    except NameError:
        print("sqr is None")
    else:
        x, y = sqr
        legalSqrs = pieceInQuestion(All, int(x + y * 8))
        location = event.pos
        rLoc = location[0] #SQUARE_SIZE
        cLoc = location[1] #SQUARE_SIZE
        Selected = All[int(x + y * 8)]
        print(Selected)

        if legalSqrs[1] in "Square":
            print("Detected!")
            # -y,+x,+y,-x
            yMAX = Selected[0] + legalSqrs[0]
            yMIN = Selected[0] - legalSqrs[0]
            xMAX = Selected[1] + legalSqrs[0]
            xMIN = Selected[1] - legalSqrs[0]
            if (((Selected[0] == rLoc) or ((yMAX == rLoc) or (yMIN == rLoc))) and (((xMAX == cLoc) or (xMIN == cLoc)) or (Selected[1] == cLoc))):
                if (Selected[0] == rLoc) and (Selected[1] == cLoc):
                    print("Not Moved")
                else:
                    All[int(x + y * 8)] = [rLoc, cLoc, Selected[2], Selected[3]]
                    print("did a thing")

        if legalSqrs[1] in "Diagnal":
            if (Selected[0] == rLoc) and (Selected[1] == cLoc):
                print("Not Moved")

        if legalSqrs[1] in "Pawn":
            if (Selected[0] + legalSqrs[0] == rLoc):
                All[x] = [rLoc, cLoc, Selected[2], Selected[3]]
            if (Selected[0] == rLoc) and (Selected[1] == cLoc):
                print("Not Moved")

        if legalSqrs[1] in "LShape":
            M = legalSqrs[0]
            print(legalSqrs[0])
            if ((Selected[0] + M[0] == rLoc) and (Selected[1] + M[1] == cLoc)) or ((Selected[1] + M[0] == cLoc) and (Selected[0] + M[1] == rLoc)):
                All[x] = [rLoc, cLoc, Selected[2], Selected[3]]
            if ((Selected[0] - M[0] == rLoc) and (Selected[1] - M[1] == cLoc)) or ((Selected[1] - M[0] == cLoc) and (Selected[0] - M[1] == rLoc)):
                All[x] = [rLoc, cLoc, Selected[2], Selected[3]]
            if ((Selected[0] + M[0] == rLoc) and (Selected[1] - M[1] == cLoc)) or ((Selected[1] + M[0] == cLoc) and (Selected[0] - M[1] == rLoc)):
                All[x] = [rLoc, cLoc, Selected[2], Selected[3]]
            if ((Selected[0] - M[0] == rLoc) and (Selected[1] + M[1] == cLoc)) or ((Selected[1] - M[0] == cLoc) and (Selected[0] + M[1] == rLoc)):
                All[x] = [rLoc, cLoc, Selected[2], Selected[3]] 
            if (Selected[0] == rLoc) and (Selected[1] == cLoc):
                    print("Not Moved")
            
        if legalSqrs[1] in "Cross":
            if (Selected[0] == rLoc) or (Selected[1] == cLoc):
                All[x] = [rLoc, cLoc, Selected[2], Selected[3]]
            if (Selected[0] == rLoc) and (Selected[1] == cLoc):
                    print("Not Moved")
        
        if legalSqrs[1] in "Cross and Diagnal":
            if (Selected[0] == rLoc) and (Selected[1] == cLoc):
                    print("Not Moved")
            # Cross
            if (Selected[0] == rLoc) or (Selected[1] == cLoc):
                All[x] = [rLoc, cLoc, Selected[2], Selected[3]]
            # Diagnal
                
        del sqr