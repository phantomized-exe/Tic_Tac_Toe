board = [
    ["01","02","03"],
    ["04","05","06"],
    ["07","08","09"],
    ["10","11","12"],
    ["13","14","15"]
]
def board_status():
    global board
    global row
    global column
    global filled_max
    line = "="
    line_num = 0
    row = 3
    column = 3
    filled_max = row*column
    print()
    for i in range(column):
        for j in range(row):
            print(" ",end="")
            print(board[i][j],end=" ")
            line_num += 4
            if j != 2:
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
def main():
    global board
    global filled
    global filled_max
    global player
    global player_input
    board_status()
    player_choice()
    if 1 <= player_input <= 3:
        if str(player_input) in board[0][0]:
            board[0][0] = player
            filled += 1
        elif str(player_input) in board[0][1]:
            board[0][1] = player
            filled += 1
        elif str(player_input) in board[0][2]:
            board[0][2] = player
            filled += 1
        else:
            print("Space already filled")
            main()
    elif 4 <= player_input <= 6:
        if str(player_input) in board[1][0]:
            board[1][0] = player
            filled += 1
        elif str(player_input) in board[1][1]:
            board[1][1] = player
            filled += 1
        elif str(player_input) in board[1][2]:
            board[1][2] = player
            filled += 1
        else:
            print("Space already filled")
            main()
    elif 7 <= player_input <= 9:
        if str(player_input) in board[2][0]:
            board[2][0] = player
            filled += 1
        elif str(player_input) in board[2][1]:
            board[2][1] = player
            filled += 1
        elif str(player_input) in board[2][2]:
            board[2][2] = player
            filled += 1
        else:
            print("Space already filled")
            main()
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
        board_status()
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