"""TicTacToeゲーム
パイソン入門コース専用のプロジェクト
©２０２３ IT KiDS株式会社
All Rights Reserved under Copyright Law
コードはオープンソースです。
ご自由にお使いください"""


board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]


def print_board():
    global board

    for row in board:
        print("".join(row))



def check_win(player):
    isWin = False
    isCats = False
    # up/down left, middle, right
    for i in range(0, 3):
        if board[i] == [player, player, player]:
            isWin = True
        elif board[i][0] == player:
            isWin = True
        elif board[i][1] == player:
            isWin = True
        elif board[i][2] == player:
            isWin = True
        elif board[i][0] == player and board[i][1] == player and board[i][2] == player:
            isWin = True
        elif board[i][2] == player and board[i][1] == player and board[i][0] == player:
            isWin = True

    return isWin


def reset_board():
    global board
    board = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]]


def run():
    global board
    x_player = "x"
    y_player = "y"

    reset_board()
    while True:
        print_board()
        print("x to move.")
        try:
            x = int(input("Enter x: "))
            y = int(input("Enter y:"))

            board[x][y] = x_player
            print_board()
            if not check_win("x"):
                print("y to move.")
                x = int(input("Enter x: "))
                y = int(input("Enter y:"))
                if board[x][y] != x_player:
                    board[x][y] = y_player
                    if not check_win("y"):
                        continue
                else:
                    print("Already occupied.")
                    continue
            elif check_win("x"):
                print("x Wins!")
            elif check_win("y"):
                print("y Wins!")

            choice = input("Play again? [y]es or anything to quit: ")
            if choice.lower() == "y":
                continue
            else:
                print("Thank you for playing.")
                break
        except IndexError:
            print("Please enter 1, 2, or 3.")
            continue
