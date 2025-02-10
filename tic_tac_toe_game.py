board = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]
]
def board_status():
    global board
    print()
    for i in range(3):
        for j in range(3):
            print(board[i][j],end=" ")
        print()
    print()
def player_choice():
    global player
    global player_input
    while True:
        try:
            player = input("X or O? ")
            player = player.upper()
            if player != "X" and player != "O":
                print("Invalid input")
                continue
            player_input = int(input("What number spot? "))
            if player_input < 0 or player_input > 9:
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
    global player
    global player_input
    board_status()
    player_choice()
    if 1 <= player_input <= 3:
        if board[0][0] in str(player_input):
            board[0][0] = player
            filled += 1
        elif board[0][1] in str(player_input):
            board[0][1] = player
            filled += 1
        elif board[0][2] in str(player_input):
            board[0][2] = player
            filled += 1
        else:
            print("Space already filled")
            main()
    elif 4 <= player_input <= 6:
        if board[1][0] in str(player_input):
            board[1][0] = player
            filled += 1
        elif board[1][1] in str(player_input):
            board[1][1] = player
            filled += 1
        elif board[1][2] in str(player_input):
            board[1][2] = player
            filled += 1
        else:
            print("Space already filled")
            main()
    if 7 <= player_input <= 9:
        if board[2][0] in str(player_input):
            board[2][0] = player
            filled += 1
        elif board[2][1] in str(player_input):
            board[2][1] = player
            filled += 1
        elif board[2][2] in str(player_input):
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
    if filled >= 9:
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
            ["1","2","3"],
            ["4","5","6"],
            ["7","8","9"]
        ]
        main()
        continue
    else:
        play_again = "n"
        break