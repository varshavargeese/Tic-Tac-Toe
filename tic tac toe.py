def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    for _ in range(9):
        print_board(board)
        player = players[turn % 2]
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter column (0-2): "))
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                return
            turn += 1
        else:
            print("Cell occupied! Try again.")
    print_board(board)
    print("It's a tie!")

tic_tac_toe()
