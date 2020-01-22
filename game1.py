# Tic Tac Toe Game 

# git push linhP  master

def make_move(board):
    """Asks a player for a move and adds the move to the board."""

    # asks user for their player #
    print("Are you player 1 or player 2?")
    player = int(input(">"))

    # asks user for a row
    print("What row do you want to place your mark at?")
    move_row = int(input(">")) - 1


    # asks user for a column
    move_col = int(input(">")) - 1


    # check if board at row and column has been taken, else put x or o there depending on player
    if board[move_row][move_col] != "-":
        print("That move has already been taken.")

    elif player == 1:
        board[move_row][move_col] = "x"
        print("You have chosen to position an x at ({},{})".format(move_row, move_col))

    else:
        board[move_row][move_col] = "o"
        print("You have chosen to position an o at ({},{})".format(move_row, move_col))



def print_board(board):
    """Prints board to show the players"""
    print()
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("---+---+---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("---+---+---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")
    print()
    


def check_win(board):
    """Checks board for a winner and returns winner"""

    pass

    # checks rows for win


    # checks columns for win


    # checks diagonals for win


def check_tie(board):
    """Checks if board is full and there's a tie"""

    pass


def play(board):
    """Main REPL function to play the game"""

    pass


#################################################################################
tic_tac_toe_board = [["-","-","-"],["-","-","-"],["-","-","-"]]
play(tic_tac_toe_board)



