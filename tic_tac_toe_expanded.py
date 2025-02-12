def board_choice():
    global row
    global column
    global multi_board
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
                multi_board.append(str(board_num))
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
    while True:
        try:
            player = input("X or O? ")
            player = player.upper()
            if player != "X" and player != "O":
                print("Invalid input")
                continue
            player_input = int(input("What number spot? "))
            if player_input < 0 or player_input > row*column:
                print("Invalid input")
                continue
            else:
                return player_input
        except ValueError:
            print("Invalid input")
            continue
filled = 0
board_choice()
def main():
    global multi_board
    global filled
    global filled_max
    global player
    global player_input
    global row
    global column
    build_board(row,column)
    filled_max = row*column
    if str(player_choice()) in str(multi_board):
        if filled_max > 9:
            position = multi_board.index(str(format(player_input,"02d")))
        else:
            position = multi_board.index(str(player_input))
        if filled_max > 9:
            multi_board[position] = " "
        else:
            multi_board[position] = ""
        multi_board[position] += player
        filled += 1
    else:
        print("Space already filled")
        main()
    formatted_list = []
    formatted_row_min = 0
    formatted_row_max = row
    for i in range(column):
        formatted_list.append(multi_board[formatted_row_min:formatted_row_max])
        formatted_row_min = formatted_row_max
        formatted_row_max += row
    for i in range(column):
        if filled_max < 10:
            if formatted_list[i-1].count(player) == row:
                build_board(row,column)
                print(f"{player} wins!")
                quit()
            #if formatted_list[i-1] == player*row:
                #build_board(row,column)
                #print(f"{player} wins! test 3")
                #return
        else:
            print(formatted_list[i].count(" " + player))
            if formatted_list[i-1].count(" " + player) == row:
                build_board(row,column)
                print(f"{player} wins!")
                quit()
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
        main()
        continue
    else:
        play_again = "n"
        quit()