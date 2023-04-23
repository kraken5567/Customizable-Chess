squares = []
from tkinter import PhotoImage

class Movement:
    squares = []

    @classmethod
    def Move(cls, squares, board_buttons):
        mover, spot = squares #squares should be 2
        print(squares)

        # get the coordinates of the old and new squares
        old_row, old_col, old_piece_type, old_color = mover
        new_col, new_row, new_piece_type, new_color = spot

        print(old_row, old_col)
        print(new_row, new_col)

        # get the corresponding buttons for the old and new squares
        old_button = (board_buttons[int(old_row)])[int(old_col)]
        new_button = (board_buttons[int(new_row)])[int(new_col)]

        print(old_button.cget('image'),new_button.cget('image'))

        # replace the image of the old button with the image of the new button
        try:
            new_button_image = PhotoImage(file=f"Pieces\\{old_color+old_piece_type}.png")
            new_button.config(image=new_button_image,command= lambda sqr = [new_col, new_row, old_piece_type, old_color]: Movement.MovedPiece(sqr, board_buttons))
            new_button.image = new_button_image


            # set the image of the new button to None
            old_button.config(image=None, command= lambda sqr = [old_row, old_col, new_piece_type, new_color]: Movement.MovedPiece(sqr, board_buttons))
            old_button.image = None
        except TypeError:
            cls.squares = []
            raise TypeError(f"Image could not be generated with: {type(old_color), type(old_piece_type)} attributes")
            
        # update the list of squares
        cls.squares = []

        return board_buttons

    @classmethod
    def MovedPiece(cls, sqr, board_buttons):
        cls.squares.append(sqr)
        print(cls.squares,(board_buttons[int(sqr[0])])[int(sqr[1])].cget('image'))
        if cls.squares[0] == [sqr[0],sqr[1],None,None]:
            cls.squares = []
            raise TypeError("Empty spot was selected first")

        if len(cls.squares) == 2:
            if Piece.Info(cls.squares):
                board_buttons = cls.Move(cls.squares, board_buttons)

        #SHOULD never run
        elif len(cls.squares) > 2:
            amountMore = len(cls.squares) - 2
            for number in range(amountMore):
                cls.squares.pop()
            if Piece.Info(cls.squares):
                board_buttons = cls.Move(cls.squares, board_buttons)
        return cls.squares

class Piece:
    def Info(squares):
        sqr0, sqr1 = squares
        row0, column0, piece0, color0 = sqr0
        row1, column1, piece1, color1 = sqr1
        if color0 != color1 and ((row0 != row1) and (column0 != column1)):
            print()

        return True
