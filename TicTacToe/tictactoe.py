import random
import copy

ttt_board = {1: " ", 2: " ", 3: " ",
             4: " ", 5: " ", 6: " ",
             7: " ", 8: " ", 9: " "}


def print_board(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])

    
def player_letter():
    letter = ""
    while not(letter == "x" or letter == "o"):
        letter = input("Choose a letter, x or o")
              
    if letter == "x":
        return ["x", "o"]
    else:
        return ["o", "x"]


def random_cpu():
    move = random.randint(1,9)
    return move

def copy_board(board):
    db = board.copy()
    return db

def ai_mofo(board, letter):
    #sets the letters
    if letter == "x":
        p_letter = "o"
    else:
        p_letter = "x"
    #sloppy way of creating duplicate boards to test winning conditions
    dupe_board = copy_board(board)
    pl_dupe_board = copy_board(board)
    # check all spaces to see if the cpu can win this turn
    for key in dupe_board.keys():
        if space_free(dupe_board, key):
            dupe_board[key] = letter
            if if_win(dupe_board, letter):
                return key
    # checks to see if the player can win to block them
    for key in pl_dupe_board.keys():
        if space_free(pl_dupe_board, key):
            pl_dupe_board[key] = p_letter
            if if_win(pl_dupe_board, p_letter):
                return key
    #for i in range(1,9):
    #    dupe_board1 = copy_board(board)
    #    if space_free(dupe_board1, i):
    #        dupe_board1[i] = letter
    #        if if_win(dupe_board1, letter):
    #            return i
    #
    #for i in range(1,9):
    #    dupe_board1 = copy_board(board)
    #    if space_free(dupe_board1, i):
    #        dupe_board1[i] = p_letter
    #        if if_win(dupe_board1, p_letter):
    #            return i
    #            
    #for i in range(1,9):
    #    dupe_board1 = copy_board(board)
    #    if space_free(dupe_board1, i):
    #        return i
            
def cpu_move(board, move, letter):
    board[move] = letter

def get_player_move():
    return input("Choose a square, 1-9")
  
def who_goes_first():
    turn = random.randint(1,2)
    if turn == 1:
        return "Computer"
    else:
        return "Player"
    
def play_again():
    choice = input("Do you want to play again? Y/N")
    return choice == "Y"


def make_move(board, move, letter):
    board[move] = letter
    
    
def if_win(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter)) 


def space_free(board, space):
    return board[space] == " "
    
def board_full(board):
    for i in board:
        if space_free(board, i):
            return False
    return True
        

def user_move(board):
    for i in range(1, 9):
        move = input("choose a square")
        if i % 2 == 0:
            board[move] = "x"
            print_board(board)
        else:
            board[move] = "o"
            print_board(board)
while True:
    ttt_board = {1: " ", 2: " ", 3: " ",
                 4: " ", 5: " ", 6: " ",
                 7: " ", 8: " ", 9: " "}
    turn = who_goes_first()
    print_board(ttt_board)
    let = player_letter()
    print("You have chosen " + let[0] + ", the " + turn + " will go first")
    game_on = True
    while game_on:
        if turn == "Player":
            print_board(ttt_board)
            print("Choose a square 1-9")
            pMove = int(input())
            if space_free(ttt_board, pMove) == True:
                make_move(ttt_board, pMove, let[0])
                winner = if_win(ttt_board, let[0])
                if winner == True:
                    print_board(ttt_board)
                    print("You win!")
                    break
                elif board_full(ttt_board):
                    print_board(ttt_board)
                    print("oh no, the board is full - it's a tie!")
                    break
                else:
                    turn = "Computer"
                    
        if turn == "Computer":
            cp_move = ai_mofo(ttt_board, let[1])
            while space_free(ttt_board, cp_move) == False:
                cp_move = ai_mofo(ttt_board, let[1])
            cpu_move(ttt_board, cp_move, let[1])
            winner = if_win(ttt_board, let[1])
            if winner == True:
                print_board(ttt_board)
                print("The computer wins!")
                break
            elif board_full(ttt_board):
                print_board(ttt_board)
                print("oh no, the board is full - it's a tie!")
                replay = play_again()
                break
            else:
                turn = "Player"
                continue
