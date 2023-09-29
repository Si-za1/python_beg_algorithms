import numpy as np

#initializing the board 
board = np.array([[" "]*3]*3)
# print (board)

#defining the players
player_1 = 'X'
player_2 = 'O'

#drawing the board 
def draw_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 9)

# draw_board(board)

#moves condition 
def make_move(board,row,col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        return False

# winning conditions 
def winner_check(board, player):
    #checking for the row
        for row in board:
            if all (cell == player for cell in row):
                  return True
    #checking for the column
        for col in range(3):
            if all(board[row][col]==player for row in range(3)):
                  return True
        
    #checking for the diagonals 
            if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
                return True
        return False

#playing the game 
current_player = player_1

while True:
    draw_board(board)
    print(f"Players' turn ${current_player}")

    #where you want to input the X or 0
    row = int(input("Enter the row (0, 1, or 2): "))
    col = int(input("Enter the column (0, 1, or 2): "))

    if make_move(board, row, col, current_player):
        if winner_check(board, current_player):
            draw_board(board)
            print(f"Player {current_player} wins!")
            break
        #for the condition of drawaw
        elif " " not in [cell for row in board for cell in row]:
            draw_board(board)
            print("It's a draw!")
            break
        else:
            current_player = player_1 if current_player == player_2 else player_2
    else:
        print("Invalid move. Try again.")



