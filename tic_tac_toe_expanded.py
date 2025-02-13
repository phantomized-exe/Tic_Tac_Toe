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
    line_break = 0
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
                line_break += 1
        print()
        if i != column-1:
            for k in range(row):
                for l in range(int(line_num/row)):
                    print(line,end="")
                if k != row-1:
                    print("|",end="")
            print()
            line_num = 0
            line_break = 0
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
    while True:
        if str(player_choice()) in str(multi_board) or str(format(player_choice(),"02d")) in str(multi_board):
            if filled_max < 10:
                position = multi_board.index(str(player_input))
                multi_board[position] = player
            else:
                position = multi_board.index(str(format(player_input,"02d")))
                multi_board[position] = " "
                multi_board[position] += player
            filled += 1
            break
        else:
            print("Space already filled")
            continue
    formatted_list = []
    formatted_row_min = 0
    formatted_row_max = row
    for i in range(column):
        formatted_list.append(multi_board[formatted_row_min:formatted_row_max])
        formatted_row_min = formatted_row_max
        formatted_row_max += row
    for i in range(column):
        for j in range(row):
            try:
                if formatted_list[i][j] == player and formatted_list[i][j+1] == player and formatted_list[i][j+2] == player or formatted_list[i][j] == " " + player and formatted_list[i][j+1] == " " + player and formatted_list[i][j+2] == " " + player:
                    build_board(row,column)
                    print(f"{player} wins!")
                    play_again()
            except IndexError:
                pass
    for i in range(column):
        for j in range(row):
            try:
                if formatted_list[i][j] == player and formatted_list[i+1][j] == player and formatted_list[i+2][j] == player or formatted_list[i][j] == " " + player and formatted_list[i+1][j] == " " + player and formatted_list[i+2][j] == " " + player:
                    build_board(row,column)
                    print(f"{player} wins!")
                    play_again()
            except IndexError:
                pass
    for i in range(column):
        for j in range(row):
            try:
                if formatted_list[i][j] == player and formatted_list[i+1][j+1] == player and formatted_list[i+2][j+2] == player or formatted_list[i][j] == " " + player and formatted_list[i+1][j+1] == " " + player and formatted_list[i+2][j+2] == " " + player:
                    build_board(row,column)
                    print(f"{player} wins!")
                    play_again()
                if formatted_list[-i-1][j] == player and formatted_list[-i-2][j+1] == player and formatted_list[-i-3][j+2] == player or formatted_list[-i-1][j] == " " + player and formatted_list[-i-2][j+1] == " " + player and formatted_list[-i-3][j+2] == " " + player:
                    build_board(row,column)
                    print(f"{player} wins!")
                    play_again()
            except IndexError:
                pass
    if filled >= filled_max:
        build_board(row,column)
        print("Tie!")
        play_again()
    else:
        main()
def play_again():
    global filled
    print()
    play_again = input("Play again? (y/n) ")
    if play_again == "y":
        filled = 0
        board_choice()
        main()
    else:
        play_again = "n"
        print()
        print("Made by Phann Boon and George Koniaris")
        quit()
if __name__ == main():
    main()