import pygame
import math
from PieceInfoer import *

def Draw(Size,winWidth,winHeight,All,ScreenMode,Change):
    frames = pygame.time.Clock()
    frames.tick(50)
    sptLists = []
    Game = True
    rendered = False
    
    pygame.init()
    dispRes = pygame.display.Info()
    ScreenMode[0] = dispRes.current_w
    ScreenMode[1] = dispRes.current_h
    
    ChessScreen = pygame.display.set_mode((int(winWidth),int(winHeight)))
    chessboard = pygame.Surface((winWidth, winHeight))

    if winWidth > winHeight:
        L = winHeight
    if winHeight > winWidth:
        L = winWidth
    if winHeight == winWidth:
        L = winWidth

    yRatio = int(L/Size[0])
    xRatio = int(L/Size[1])

    for col in range(Size[1]):
        for row in range(Size[0]):
            image_x = row * L/Size[0]
            image_y = col * L/Size[1]
            if (row + col) % 2 == 0:
                color = (50, 50, 50)
            else:
                color = (205, 205, 205)
            
            pygame.draw.rect(chessboard, color, (image_x, image_y, yRatio, xRatio))
            #square = pygame.Rect(image_x,image_y,winHeight/Size[0],winWidth/Size[1])
    
    x = (ChessScreen.get_width() - chessboard.get_width()) // 2
    y = (ChessScreen.get_height() - chessboard.get_height()) // 2
    ChessScreen.blit(chessboard, (x, y))

    exit = pygame.Rect(winWidth-20, 0, 20, 10)
    pygame.draw.rect(ChessScreen, (255, 0, 0), (winWidth-20, 0, 20,10))

    full = pygame.Rect(winWidth-40, 0, 20, 10)
    pygame.draw.rect(ChessScreen, (255, 255, 0), (winWidth-40, 0, 20,10))

    
    if rendered != True:
        for i in range(len(All)):
            l = All[i]
            a = l
            y_val = (a[0])*(yRatio)
            x_val = (a[1])*(xRatio)
            imgName = pygame.image.load("Pieces/"+str(a[3])+str(a[2])+"/"+str(a[3])+str(a[2])+".png")
            if xRatio > yRatio:
                imgName = pygame.transform.scale(imgName, (yRatio, yRatio))
            elif yRatio > xRatio:
                imgName = pygame.transform.scale(imgName, (xRatio, xRatio))
            elif xRatio == yRatio:
                imgName = pygame.transform.scale(imgName, (xRatio, yRatio))
            ChessScreen.blit(imgName, (x_val, y_val))

            sptLists.append(x_val)
            sptLists.append(y_val)
        rendered = True
    if Change == True:
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if exit.collidepoint(event.pos):
                print("Button pressed!")
                Game = False
            if full.collidepoint(event.pos):
                print("Toggled Screen Mode!")
                ScreenMode != ScreenMode
            for x in range(int(len(sptLists)/2)):
                a = sptLists[2*x]
                b = sptLists[2*x + 1]
                location = pygame.mouse.get_pos()
                xMax = a + xRatio
                yMax = b + yRatio
                if (location[0] >= a and location[0] <= xMax) and (location[1] >= b and location[1] <= yMax):
                    global sqr
                    sqr = [x,(location[0]/xRatio),(location[1]/yRatio)]
                    print(sqr)
        
        if event.type == pygame.MOUSEBUTTONUP:
            try: sqr
            except NameError: print("sqr is None")
            else:
                u = 0
                x = sqr[0]
                legalSqrs = pieceInQuestion(All,x)
                location = pygame.mouse.get_pos()
                cLoc = math.trunc(location[0]/xRatio)
                rLoc = math.trunc(location[1]/yRatio)
                Selected = All[x]
                print(Selected)
                
                if legalSqrs[1] in "Square":
                    print("Detected!")
                    #-y,+x,+y,-x
                    yMAX = Selected[0] + legalSqrs[0]
                    yMIN = Selected[0] - legalSqrs[0]
                    xMAX = Selected[1] + legalSqrs[0]
                    xMIN = Selected[1] - legalSqrs[0]
                    if (((Selected[0] == rLoc) or ((yMAX == rLoc) or (yMIN == rLoc))) and (((xMAX == cLoc) or (xMIN == cLoc)) or (Selected[1] == cLoc))):
                        if (Selected[0] == rLoc) and (Selected[1] == cLoc):
                            print("Not Moved")
                        else:
                            All[x] = [rLoc, cLoc, Selected[2], Selected[3]]
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
    return Game