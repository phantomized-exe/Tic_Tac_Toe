import random
filled = 0
def board_choice(bot_choice):
    # determines the size of the board for 2 players, if 1 player selected, sets board to 3x3
    global multi_board
    if bot_choice == "n":
        try:
            row = int(input("What row size? "))
            column = int(input("What column size? "))
        except ValueError:
            print("Invalid input")
            board_choice()
    else:
        row = 3
        column = 3
    board_area = {"Row": row, "Column": column}
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
    return board_area
    
def build_board(row,column):
    # prints the updated board
    global multi_board
    line = "="
    line_num = 0
    list_num = 0
    list_value = row*column
    line_break = 0
    print()
    for i in range(column):
        for j in range(row):
            # prints the numbers evenly spaced out
            print(" ",end="")
            print(multi_board[list_num],end=" ")
            list_num += 1
            if list_value < 10:
                line_num += 3
            else:
                line_num += 4
            if j != row-1:
                # prints the vertical lines dividing the numbers
                print("|",end="")
                line_break += 1
        print()
        if i != column-1:
            for k in range(row):
                # prints the horizontal lines dividing the numbers
                for l in range(int(line_num/row)):
                    print(line,end="")
                if k != row-1:
                    print("|",end="")
            print()
            line_num = 0
            line_break = 0
    print()
def player_choice(row,column,bot_choice):
    # determines X or O and where they go
    global player
    global player_input
    global multi_board
    while True:
        try:
            if bot_choice == "y":
                player = "X"
            else:
                player = input("X or O? ")
                player = player.upper()
                if player != "X" and player != "O":
                    print("Invalid input")
                    continue    
            player_input = int(input("What number spot? "))
            if player_input < 0 or player_input > row*column:
                print("Invalid input")
                continue
            elif multi_board[player_input-1] == "X" or multi_board[player_input-1] == " X" or multi_board[player_input-1] == "O" or multi_board[player_input-1] == " O":
                print("Space already filled")
                continue
            else:
                return player_input
        except ValueError:
            print("Invalid input")
            continue
def rand_move(row,column,filled_max):
    # if the bot has no logical move it moves randomly
    print("Random")
    while True:
        rand_row = random.randint(0,row)
        rand_column = random.randint(0,column)
        if multi_board[rand_row+rand_column] != "X" and multi_board[rand_row+rand_column] != " X" and multi_board[rand_row+rand_column] != "O" and multi_board[rand_row+rand_column] != " O":
            if filled_max < 10:
                multi_board[rand_row+rand_column] = "O"
                return
            else:
                multi_board[rand_row+rand_column] = " O"
                return
        else:
            continue
def robot_move(row,column,formatted_list,filled_max):
    # the robot logic
    global multi_board
    global filled
    global player
    formatted_row_min = 0
    formatted_row_max = row
    for i in range(column):
        formatted_list.append(multi_board[formatted_row_min:formatted_row_max])
        formatted_row_min = formatted_row_max
        formatted_row_max += row
    for h in range(2):
        # checks if either player is about to win
        if h == 0:
            player = "O"
        else:
            player = "X"
        for i in range(column):
            try:
                # checks if a horizontal line has 2 Xs
                if formatted_list[i].count("X") >= 2 or formatted_list[i].count(" X") >= 2 or formatted_list[i].count("O") >= 2 or formatted_list[i].count(" O") >= 2:
                    for j in range(row):
                        # finds the blank space and fills it with O
                        if formatted_list[i][j] != "X" and formatted_list[i][j] != " X" and formatted_list[i][j] != "O" and formatted_list[i][j] != " O":
                            if filled_max < 10:
                                total_count = multi_board.index(str(formatted_list[i][j]))
                                multi_board[total_count] = "O"
                                formatted_list[i][j] = "O"
                                filled += 1
                                return
                            else:
                                total_count = multi_board.index(str(format(int(formatted_list[i][j]),"02d")))
                                multi_board[total_count] = " O"
                                formatted_list[i][j] = " O"
                                filled += 1
                                return
            except IndexError:
                pass
        for i in range(column):
            for j in range(row):
                try:
                    # if player is about to win horizontally, bot blocks them
                    if formatted_list[i][j] == player or formatted_list[i][j] == " " + player:
                        if formatted_list[i+1][j] == player or formatted_list[i+1][j] == " " + player:
                            if formatted_list[i+2][j] !="X" and formatted_list[i+2][j] != " X" and formatted_list[i+2][j] != "O" and formatted_list[i+2][j] != " O":
                                if filled_max < 10:
                                    total_count = multi_board.index(str(formatted_list[i+2][j]))
                                    multi_board[total_count] = "O"
                                    formatted_list[i+2][j] = "O"
                                    filled += 1
                                    return
                                else:
                                    total_count = multi_board.index(str(format(int(formatted_list[i+2][j]),"02d")))
                                    multi_board[total_count] = " O"
                                    formatted_list[i+2][j] = " O"
                                    filled += 1
                                    return
                except IndexError:
                    try:
                        # if player 2 in a row too far down, bot will block them higher up
                        if formatted_list[i+1][j] == player or formatted_list[i+1][j] == " " + player:
                            if formatted_list[i-1][j] != "X" and formatted_list[i-1][j] != " X" and formatted_list[i-1][j] != "O" and formatted_list[i-1][j] != " O":
                                if filled_max < 10:
                                    total_count = multi_board.index(str(formatted_list[i-1][j]))
                                    multi_board[total_count] = "O"
                                    formatted_list[i-1][j] = "O"
                                    filled += 1
                                    return
                                else:
                                    total_count = multi_board.index(str(format(int(formatted_list[i-1][j]),"02d")))
                                    multi_board[total_count] = " O"
                                    formatted_list[i-1][j] = " O"
                                    filled += 1
                                    return
                    except IndexError:
                        pass
        for i in range(column):
            for j in range(row):
                # checks if the player is about to get diagonal 3 in a row
                try:
                    if formatted_list[i][j] == player or formatted_list[i][j] == " " + player:
                        if formatted_list[i+1][j+1] == player or formatted_list[i+1][j+1] == " " + player:
                            if formatted_list[i+2][j+2] != "X" and formatted_list[i+2][j+2] != " X" and formatted_list[i+2][j+2] != "O" and formatted_list[i+2][j+2] != " O":
                                if filled_max < 10:
                                    total_count = multi_board.index(str(formatted_list[i+2][j+2]))
                                    multi_board[total_count] = "O"
                                    formatted_list[i+2][j+2] = "O"
                                    filled += 1
                                    return
                                else:
                                    total_count = multi_board.index(str(format(int(formatted_list[i+2][j+2]),"02d")))
                                    multi_board[total_count] = " O"
                                    formatted_list[i+2][j+2] = " O"
                                    filled += 1
                                    return
                        elif formatted_list[i+2][j+2] == player or formatted_list[i+2][j+2] == " " + player:
                            if formatted_list[i+1][j+1] != "X" and formatted_list[i+1][j+1] != " X" and formatted_list[i+1][j+1] != "O" and formatted_list[i+1][j+1] != " O":
                                if filled_max < 10:
                                    total_count = multi_board.index(str(formatted_list[i+1][j+1]))
                                    multi_board[total_count] = "O"
                                    formatted_list[i+1][j+1] = "O"
                                    filled += 1
                                    return
                                else:
                                    total_count = multi_board.index(str(format(int(formatted_list[i+1][j+1]),"02d")))
                                    multi_board[total_count] = " O"
                                    formatted_list[i+1][j+1] = " O"
                                    filled += 1
                                    return
                except IndexError:
                    try:
                        # if player diagonal too far down, bot blocks higher up
                        if formatted_list[i+1][j+1] == player or formatted_list[i+1][j+1] == " " + player:
                            if formatted_list[i-1][j-1] != "X" and formatted_list[i-1][j-1] != " X" and formatted_list[i-1][j] != "O" and formatted_list[i-1][j] != " O":
                                if filled_max < 10:
                                    total_count = multi_board.index(str(formatted_list[i-1][j-1]))
                                    multi_board[total_count] = "O"
                                    formatted_list[i-1][j-1] = "O"
                                    filled += 1
                                    return
                                else:
                                    total_count = multi_board.index(str(format(int(formatted_list[i-1][j-1]),"02d")))
                                    multi_board[total_count] = " O"
                                    formatted_list[i-1][j-1] = " O"
                                    filled += 1
                                    return
                    except IndexError:
                        pass
                try:
                    # checks for backwards diagonals
                    if formatted_list[-i][j] == player or formatted_list[-i][j] == " " + player:
                        if formatted_list[-i-1][j+1] == player or formatted_list[-i-1][j+1] == " " + player:
                            if formatted_list[-i-2][j+2] != "X" and formatted_list[-i-2][j+2] != " X" and formatted_list[-i-2][j+2] != "O" and formatted_list[-i-2][j+2] != " O":
                                if filled_max < 10:
                                    total_count = multi_board.index(str(formatted_list[-i-2][j+2]))
                                    multi_board[total_count] = "O"
                                    formatted_list[-i-2][j+2] = "O"
                                    filled += 1
                                    return
                                else:
                                    total_count = multi_board.index(str(format(int(formatted_list[-i-2][j+2]),"02d")))
                                    multi_board[total_count] = " O"
                                    formatted_list[-i-2][j+2] = " O"
                                    filled += 1
                                    return
                        elif formatted_list[-i-2][j+2] == player or formatted_list[-i-2][j+2] == " " + player:
                            if formatted_list[-i-1][j+1] != "X" and formatted_list[-i-1][j+1] != " X" and formatted_list[-i-1][j+1] != "O" and formatted_list[-i-1][j+1] != " O":
                                if filled_max < 10:
                                    total_count = multi_board.index(str(formatted_list[-i-1][j+1]))
                                    multi_board[total_count] = "O"
                                    formatted_list[-i-1][j+1] = "O"
                                    filled += 1
                                    return
                                else:
                                    total_count = multi_board.index(str(format(int(formatted_list[-i-1][j+1]),"02d")))
                                    multi_board[total_count] = " O"
                                    formatted_list[-i-1][j+1] = " O"
                                    filled += 1
                                    return
                except IndexError:
                    try:
                        if formatted_list[-i-1][j+1] == player or formatted_list[-i-1][j+1] == " " + player:
                            if formatted_list[-i+1][j-1] != "X" and formatted_list[-i+1][j-1] != " X" and formatted_list[-i+1][j] != "O" and formatted_list[-i+1][j] != " O":
                                if filled_max < 10:
                                    total_count = multi_board.index(str(formatted_list[-i+1][j-1]))
                                    multi_board[total_count] = "O"
                                    formatted_list[-i+1][j-1] = "O"
                                    filled += 1
                                    return
                                else:
                                    total_count = multi_board.index(str(format(int(formatted_list[-i+1][j-1]),"02d")))
                                    multi_board[total_count] = " O"
                                    formatted_list[-i+1][j-1] = " O"
                                    filled += 1
                                    return
                    except IndexError:
                        pass
    rand_move(row,column,filled_max)
    filled += 1
    return
def main(board_area,bot_choice):
    # calls the other functions depending on player inputs
    global multi_board
    global player
    global player_input
    global filled
    row = board_area["Row"]
    column = board_area["Column"]
    build_board(board_area["Row"],board_area["Column"])
    filled_max = row*column
    player_choice(row,column,bot_choice)
    if filled_max < 10:
        position = multi_board.index(str(player_input))
        multi_board[position] = player
    else:
        position = multi_board.index(str(format(player_input,"02d")))
        multi_board[position] = " "
        multi_board[position] += player
    filled += 1
    # checks if playing 2 player or with bot
    if bot_choice == "y":
        check_win(row,column,filled,filled_max)
        robot_move(row,column,formatted_list,filled_max)
    check_win(row,column,filled,filled_max)
    main(board_area,bot_choice)
def check_win(row,column,filled,filled_max):
    # determines win, tie, or continue game
    global player
    global formatted_list
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
                # checks for horizontal win
                if formatted_list[i][j] == player and formatted_list[i][j+1] == player and formatted_list[i][j+2] == player or formatted_list[i][j] == " " + player and formatted_list[i][j+1] == " " + player and formatted_list[i][j+2] == " " + player:
                    build_board(row,column)
                    print(f"{player} wins!")
                    play_again()
            except IndexError:
                pass
    for i in range(column):
        for j in range(row):
            try:
                # checks for vertical win
                if formatted_list[i][j] == player and formatted_list[i+1][j] == player and formatted_list[i+2][j] == player or formatted_list[i][j] == " " + player and formatted_list[i+1][j] == " " + player and formatted_list[i+2][j] == " " + player:
                    build_board(row,column)
                    print(f"{player} wins!")
                    play_again()
            except IndexError:
                pass
    for i in range(column):
        for j in range(row):
            try:
                # checks for diagonal win
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
    # checks if all the squares are filled
    if filled >= filled_max:
        build_board(row,column)
        print("Tie!")
        play_again()
    else:
        return
def play_again():
    # determines if main should restart
    global filled
    print()
    play_again = input("Play again? (y/n) ")
    if play_again == "y":
        filled = 0
        while True:
            try:
                bot_choice = input("Use a bot? (y/n) ")
                if bot_choice != "y" and bot_choice != "n":
                    print("Invalid input")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid input")
                continue
        board_area = board_choice(bot_choice)
        main(board_area,bot_choice)
    else:
        play_again = "n"
        print()
        print("Made by Phann Boon and George Koniaris")
        quit()
while True:
    # decides if the game is played with 2 players or bot
    try:
        bot_choice = input("Use a bot? (y/n) ")
        if bot_choice != "y" and bot_choice != "n":
            print("Invalid input")
            continue
        else:
            break
    except ValueError:
        print("Invalid input")
        continue
board_area = board_choice(bot_choice)
if __name__ == main(board_area,bot_choice):
    main(board_area,bot_choice)