board = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]
]
def player_choice():
    while True:
        try:
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
    tie = "Nobody wins due to a tie"
    x_win = "X wins!"
    y_win = "Y wins!"
    for i in range(3):
        for j in range(3):
            print(board[i][j],end=" ")
        print()
    print("X: ",end="")
    x_input = player_choice()
    if 1 <= x_input <= 3:
        if board[0][0] in str(x_input):
            board[0][0] = "X"
            filled += 1
        elif board[0][1] in str(x_input):
            board[0][1] = "X"
            filled += 1
        elif board[0][2] in str(x_input):
            board[0][2] = "X"
            filled += 1
        else:
            print("Space already filled")
            main()
    elif 4 <= x_input <= 6:
        if board[1][0] in str(x_input):
            board[1][0] = "X"
            filled += 1
        elif board[1][1] in str(x_input):
            board[1][1] = "X"
            filled += 1
        elif board[1][2] in str(x_input):
            board[1][2] = "X"
            filled += 1
        else:
            print("Space already filled")
            main()
    if 7 <= x_input <= 9:
        if board[2][0] in str(x_input):
            board[2][0] = "X"
            filled += 1
        elif board[2][1] in str(x_input):
            board[2][1] = "X"
            filled += 1
        elif board[2][2] in str(x_input):
            board[2][2] = "X"
            filled += 1
        else:
            print("Space already filled")
            main()
    if board[0] == ["X","X","X"] or board[1] == ["X","X","X"] or board[2] == ["X","X","X"]:
        print()
        return x_win
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print()
        return x_win
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print()
        return x_win
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print()
        return x_win
    if filled >= 9:
        print()
        return tie
    for i in range(3):
        for j in range(3):
            print(board[i][j],end=" ")
        print()
    while filled < 9:
        print("Y: ",end="")
        y_input = player_choice()
        if 1 <= y_input <= 3:
            if board[0][0] in str(y_input):
                board[0][0] = "Y"
                filled += 1
            elif board[0][1] in str(y_input):
                board[0][1] = "Y"
                filled += 1
            elif board[0][2] in str(y_input):
                board[0][2] = "Y"
                filled += 1
            else:
                print("Space already filled")
                continue
        elif 4 <= y_input <= 6:
            if board[1][0] in str(y_input):
                board[1][0] = "Y"
                filled += 1
            elif board[1][1] in str(y_input):
                board[1][1] = "Y"
                filled += 1
            elif board[1][2] in str(y_input):
                board[1][2] = "Y"
                filled += 1
            else:
                print("Space already filled")
                continue
        if 7 <= y_input <= 9:
            if board[2][0] in str(y_input):
                board[2][0] = "Y"
                filled += 1
            elif board[2][1] in str(y_input):
                board[2][1] = "Y"
                filled += 1
            elif board[2][2] in str(y_input):
                board[2][2] = "Y"
                filled += 1
            else:
                print("Space already filled")
                continue
        if board[0] == ["Y","Y","Y"] or board[1] == ["Y","Y","Y"] or board[2] == ["Y","Y","Y"]:
            print()
            return y_win
        elif board[0][0] == "Y" and board[1][0] == "Y" and board[2][0] == "Y":
            print()
            return y_win
        elif board[0][1] == "Y" and board[1][1] == "Y" and board[2][1] == "Y":
            print()
            return y_win
        elif board[0][2] == "Y" and board[1][2] == "Y" and board[2][2] == "Y":
            print()
            return y_win
        if filled >= 9:
            print()
            return tie
        else:
            main()
print(main())
