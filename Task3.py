def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
        
def check_win(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw(board):
    return all([cell != " " for row in board for cell in row])

def init_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def play_round():
    board = init_board()
    first_player = "X"
    
    while True: 
        print_board(board)
        print(f"Player {first_player}'s turn.")
        
        move = input("Enter your move as row, col: ")
        try:
            row, col = map(int, move.split(","))
            if board[row - 1][col - 1] != " ":
                print("This spot is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid move as row,col (eg., 1,2).")
            continue
        
        board[row - 1][col - 1] = first_player
        
        if check_win(board, first_player):
            print_board(board)
            print(f"Player {first_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        first_player = "O" if first_player == "X" else "X"
        
        
def tic_tac_toe():
    while True:
        play_round()
        choice = input("Do you want to play again?(Y/N):").strip().lower()
        if choice != "yes":
            print("Thanks for Playing! ")
            break
        
tic_tac_toe()       
                