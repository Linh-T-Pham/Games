# OBJECTS

# 1. Player 
# 2. Move
# 3. Board
# 4. Game 

# Atrribute (data) and Methods (behaviors) in Tic-Tac-Toe
# 1. Player
    ## Attributes:
        # 1. game_piece: When player is X or O in the board
        # 2. name: name of player 

# 2. Move 
    ## Attributes:
        # 1. author: who made the move
        # 2. position: where the move is placed on the board

# 3. Board
    ## Attributes
        # 1. moves: all the moves currently on the board
    ## Methods
        # 1. display: print out the board for users to see it
        # 2. add_move: takes a move as an argument, adds it to moves atrribute 
# 4. Game
    ## Attributes:
        # 1. board: the playing board for the game
        # 2. player1: first player in the game
        # 3. player2: second player in the game
        # 4. started_at: when the game started 
        # 5. finished_at: When the game ended 


# Leetcode # 794

"""
>>> board(["0", "  ", "  "])
false
>>> board(["XOX", " X ", "  "])
false
>>> board(["XXX", "  ", "OOO"])
false 
>>> board(["XOX", "O O", "XOX"])
true 
"""


def validTictacToe (self, board): 

    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True 

    else:
        return False 





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** AWESOME!. GO GO GO!\n")