# - Create 3 separate files:
# 1) ChessPiece.py
# - Chess pieces are what I will add to the squares on the board
#  - Chess pieces can move in L-shape(Knight), can move straight or diagonally 
# -  Chess pieces have a name and the number of squares it traverse per move

#ChessPiece.py ***********************

Color = None
Type = None

ListofPieces = [‘Rook’, ‘Knight’, ‘Pawn’, ‘King’, ‘Queen’, ‘Bishop’,’Random’]

def __init__(self, dict_args):
    self.Type = dict_args['Type']
    self.Color = dict_args['Color']

def __str__(self):
    if self.Type in [‘Rook’, ‘Knight’, ‘Pawn’, ‘King’, ‘Queen’, ‘Bishop’,’Random’]:
        color = self.Color[0]
        if (self.Type != 'Knight'):
            pieceType = self.Type[0]
        else:
            pieceType = 'N'

        return color.lower() + pieceType.upper()
    else:
        return ' '

def getType(self):
    return self.Type
    

# 2) ChessBoard.py *************************

# Gameboard has 2 classes. The first one is 2D array which contains chess pieces and the second one is 
# GameBoard class 

class Square(object):
    Row = 0
    Column = 0
    Occupied = False
    Piece = " "
    ListofColumns = ["A", "B", "C", "D", "E", "F", "G", "H"]
    ListofCoordinates = [1,2,3,4,5,6,7,8]

    def __init__(self, row, column):
        self.Row = row
        self.Column = column

    """Return true if there is a piece"""
    def occupied(self):
        return self.Occupied

    """Sets the piece for a square and set the occupied variable"""
    def setPiece(self, piece):
        if piece.Type == "":
            self.Occupied = False
        else:
            self.Occupied = True 
        self.Piece = piece 

    """Return the piece attached to this sqaure instance"""
    def getPiece(self):
        return self.Piece 

class GameBoard(object):

    Matrix = [[0 for x in range(9)] for j in range(9)]
    Board = [[0 for x in range(9)] for j in range(9)]

    ListofColumns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    def __init__(self):
        for row in range(0,9):
            for column in range(0,9):
                self.Matrix[row][column] = Square(row, column)
                self.Matrix[row][column].Occupied = True

        for row in range(0,9):
            self.addPiece('Black', 'Pawn', 1, column)
            self.addPiece('White', 'Pawn', 6, column)

# 3) Game.py *******************
from ChessPiece import ChessPiece

class Game(object):
    player1 = {}
    player2 = {}
    Gameover = False
    Chessboard = GameBoard()

    ListofColumns = ['A', 'B', 'C','D', 'E', 'F', 'G', 'H']
    ListofCoordinates = [1,2,3,4,5,6,7,8]

    def __init__(self):
        print"Welcome to the game"
    def information(self, name, color, dicty):
        dicty['Name'] = name
        dicty['Color'] = color

    def position_to_xCoor(self, position):
        for i in range(0,8):
            if self.ListofColumns[i] == position[0]:
                row = i + 1
        return row 

    def position_to_yCoor(self, position):
        column = 8 - int(position[1])
        return column

    def validmove(self, color, row1, column1, row2, column2):

    def blockedMove(Self, color, rise, run, column1, column2, row1, row2):

    def check(color, piece, rise, run, colum, row):

    def KingDead(self, color):

    def promotePawn(self, piece, row1, column1, row2):

    def run(self):
        

