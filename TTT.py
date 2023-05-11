import random

def make_move(brd, player):

    legal = []
    count = 0

    for c in brd:
        if c == " ":
            legal.append(count)
        count += 1

    next = random.choice(legal)

    brd[next] = player

    return brd


def simulate(board, idx):

    board[idx] = "O"

    score = 0

    for _ in range(1000):

        brd = board.copy()

        ply = "O"
        while check_win(brd, ply) == "not yet":

            if ply == "X":
                ply = "O"
            else:
                ply = "X"
            brd = make_move(brd,ply)
        
        tmp = check_win(brd,ply)
 
        if tmp != "tie":
            if tmp == "O":
                score += 1
            elif tmp == "X":
                score -= 2
        else:
            score += 1


    return score



def MCTS(board):
    
    next = -1
    wins = -10000
    loc = 1

    for c in board:
        if c == " ":
            
            brd = board.copy()
            score = simulate(brd, loc - 1)
            if score > wins:
                wins = score
                next = loc

        loc += 1

    board[next - 1] = "O"

    return board        




def print_board(board):
    print("     |     |")
    print("  " + board[0] + "  |  " + board[1] + "  |  " + board[2])
    print("_____|_____|_____")
 
    print("     |     |")
    print("  " + board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("_____|_____|_____")
 
    print("     |     |")
    print("  " + board[6] + "  |  " + board[7] + "  |  " + board[8])
    print("     |     |")
 

def check_win(board, player):

    win = "not yet"
    if (board[0] == player and board[1] == player and board[2] == player) or \
        (board[3] == player and board[4] == player and board[5] == player) or \
        (board[6] == player and board[7] == player and board[8] == player) or \
        (board[0] == player and board[3] == player and board[6] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[0] == player and board[4] == player and board[8] == player) or \
        (board[2] == player and board[4] == player and board[6] == player):
        win = player

    if win == "not yet":
        count = 0
        for i in board:
            if i != " ":
                count += 1
            if count == 9:
                win = "tie"
            
    return win


def tictactoe():
    print("Welcome to Tic Tac Toe!")
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player1 = "X"
    player2 = "O"
    current_player = player1
    game_over = False

    print_board(board)
    while not game_over:
        
        if current_player == player1:
            position = input("Player enter a position (1-9): ")
            while not position.isdigit() or int(position) < 1 or int(position) > 9 or board[int(position) - 1] in [player1, player2]:
                position = input("Invalid input. Player " + current_player + ", enter a position (1-9): ")
            board[int(position) - 1] = current_player
            print_board(board)
        else:
            print("AI makes move:")
            board = MCTS(board)
            print_board(board)

        if check_win(board, current_player) == current_player:
            print("Congratulations, Player " + current_player + " wins!")
            game_over = True
        elif check_win(board,current_player) == "tie":
            game_over = True
            print("Oops, we are tied")
        else:
            current_player = player2 if current_player == player1 else player1

tictactoe()
