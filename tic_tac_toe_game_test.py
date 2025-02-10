board = [
    ["E","E","E"],
    ["E","E","E"],
    ["E","E","E"]
]
def main():
    global board
    for i in range(3):
        for j in range(3):
            print(board[i][j],end=" ")
        print()
    while True:
        try:
            x_row = int(input("X: What row? (0-2) "))
            if x_row < 0 or x_row > 2:
                print("Invalid input")
                continue
            else:
                break
        except ValueError:
            print("Invalid input")
            continue
    while True:
        try:
            x_column = int(input("X: What column? (0-2) "))
            if x_column < 0 or x_column > 2:
                print("Invalid input")
                continue
            else:
                break
        except ValueError:
            print("Invalid input")
            continue
    if board[x_row][x_column] == "E":
        board[x_row][x_column] = "X"
    else:
        print("Space already filled")
        main()
    if board[0] == ["X","X","X"] or board[1] == ["X","X","X"] or board[2] == ["X","X","X"]:
        print("X wins!")
        return
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print("X wins!")
        return
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print("X wins!")
        return
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print("X wins!")
        return
    for i in range(3):
        for j in range(3):
            print(board[i][j],end=" ")
        print()
    while True:
        try:
            y_row = int(input("Y: What row? (0-2) "))
            if y_row < 0 or y_row > 2:
                print("Invalid input")
                continue
            else:
                break
        except ValueError:
            print("Invalid input")
            continue
    while True:
        try:
            y_column = int(input("Y: What column? (0-2) "))
            if y_column < 0 or y_column > 2:
                print("Invalid input")
                continue
            else:
                break
        except ValueError:
            print("Invalid input")
            continue
    if board[y_row][y_column] == "E":
        board[y_row][y_column] = "Y"
    else:
        print("Space already filled")
        main()
    if board[0] == ["Y","Y","Y"] or board[1] == ["Y","Y","Y"] or board[2] == ["Y","Y","Y"]:
        print("Y wins!")
        return
    elif board[0][0] == "Y" and board[1][0] == "Y" and board[2][0] == "Y":
        print("Y wins!")
        return
    elif board[0][1] == "Y" and board[1][1] == "Y" and board[2][1] == "Y":
        print("Y wins!")
        return
    elif board[0][2] == "Y" and board[1][2] == "Y" and board[2][2] == "Y":
        print("Y wins!")
        return
    if board not in "E":
        print("Nobody wins due to a tie.")
    else:
        main()
main()
