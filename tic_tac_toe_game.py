board = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]
]
def main():
    global board
    for i in range(3):
        for j in range(3):
            print(board[i][j],end=" ")
        print()
    while True:
        try:
            x_row = int(input("X: What number spot? "))
            if x_row < 0 or x_row > 9:
                print("Invalid input")
                continue
            else:
                break
        except ValueError:
            print("Invalid input")
            continue
    if