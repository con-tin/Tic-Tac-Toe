board = ['*','*',"*",
         '*','*','*',
         '*','*','*',]

def display_board():
    global board
    print(board[0] + ' | ' + board[1]  + ' | ' +board[2])
    print(board[3] + ' | ' + board[4]  + ' | ' +board[5])
    print(board[6] + ' | ' + board[7]  + ' | ' +board[8])  


def play_game():
    global board
    board = ['*', '*', "*",
             '*', '*', '*',
             '*', '*', '*', ]

    display_board()
    handle_turn()

def check():
    global board
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        print("Win")
        print("_________________________")
        play_game()


def handle_turn():
    global board
    for turn in range(1, 10):
        print(f"Ход: {turn}")
        if turn % 2 == 0:
            turn_char = "0"
            print("Ходят нолики")
            position = input("Choose a position from 1-9: ")
            position = int(position) - 1

            board[position] = "0"
            display_board()
            check()

        else:
            turn_char = "X"
            print("Ходят крестики")
            position = input("Choose a position from 1-9: ")
            position = int(position) - 1

            board[position] = "X"
            display_board()
            check()





play_game()