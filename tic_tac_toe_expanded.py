while True:
    try:
        row = int(input("What row size? "))
        column = int(input("What column size? "))
    except ValueError:
        print("Invalid input")
        continue
    else:
        break
multi_board = []
board_num = 0
list_value = row*column
for i in range(column):
    for j in range(row):
        board_num += 1
        if list_value < 10:
            multi_board.append(str(board_num))#format(board_num,"02d")))
        else:
            multi_board.append(str(format(board_num,"02d")))
    
def build_board(row,column):
    global multi_board
    line = "="
    line_num = 0
    list_num = 0
    list_value = row*column
    print()
    for i in range(column):
        for j in range(row):
            print(" ",end="")
            print(multi_board[list_num],end=" ")
            list_num += 1
            if list_value < 10:
                line_num += 3
            else:
                line_num += 4
            if j != row-1:
                print("|",end="")
                line_num += 1
        print()
        if i != column-1:
            print(line*line_num)
            line_num = 0
    print()
def player_choice():
    global player
    global player_input
    global row
    global column
    try:
        player = input("X or O? ")
        player = player.upper()
        if player != "X" and player != "O":
            print("Invalid input")
            player_choice()
        player_input = int(input("What number spot? "))
        if player_input < 0 or player_input > row*column:
            print("Invalid input")
            player_choice()
        else:
            return player_input
    except ValueError:
        print("Invalid input")
        player_choice()
filled = 0
def main():
    global multi_board
    global filled
    global filled_max
    global player
    global player_input
    global row
    global column
    filled_max = row*column
    build_board(row,column)
    if str(player_choice()) in str(multi_board):
        position = multi_board.index(str(format(player_input,"02d")))
        multi_board[position] = " " + player
        filled += 1
    else:
        print("Space already filled")
        main()
    build_board(row,column)
    if board[0] == [player,player,player] or board[1] == [player,player,player] or board[2] == [player,player,player]:
        board_status()
        print(f"{player} wins!")
        filled = 9
        return
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        board_status()
        print(f"{player} wins!")
        filled = 9
        return
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        board_status()
        print(f"{player} wins!")
        filled = 9
        return
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        board_status()
        print(f"{player} wins!")
        filled = 9
        return
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        board_status()
        print(f"{player} wins!")
        filled = 9
        return
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        board_status()
        print(f"{player} wins!")
        filled = 9
        return
    if filled >= filled_max:
        build_board()
        print("Tie!")
        return
    else:
        main()
main()
play_again = "y"
while play_again == "y":
    print()
    play_again = input("Play again? (y/n) ")
    if play_again == "y":
        filled = 0
        board = [
            ["01","02","03"],
            ["04","05","06"],
            ["07","08","09"]
        ]
        main()
        continue
    else:
        play_again = "n"
        break