sample_board = [
    [5, 0, 9, 4, 0, 0, 0, 3, 0],
    [0, 0, 3, 0, 0, 0, 6, 9, 0],
    [0, 1, 0, 0, 0, 9, 0, 0, 5],
    [0, 5, 0, 1, 8, 0, 0, 0, 0],
    [3, 0, 0, 0, 5, 0, 0, 0, 7],
    [0, 0, 4, 0, 9, 6, 0, 5, 0],
    [9, 0, 0, 8, 0, 0, 0, 7, 0],
    [0, 3, 8, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 9, 0, 7, 1, 0, 3]
]


def solve(bo):

    find = find_empty(bo)

    if find:
        row, col = find  # locate coordinates of empty square

    else:
        return True  # solved if no empty squares

    for i in range(1, 10):
        if valid(bo, (row, col), i):
            bo[row][col] = i  # if is it a valid number

            if solve(bo):
                return True  # solved if now no empty squares

            bo[row][col] = 0  # backtrack

    return False


def find_empty(bo):

    for i in range(9):  # loop over row
        for j in range(9):  # loop over col
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


def valid(bo, pos, num):

    # Check for duplicates in row
    for i in range(9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check for duplicates in column
    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check for duplicates in box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def main():
    print("       Sudoku:")
    print_board(sample_board)

    print("\n" + "      Solution:")
    solve(sample_board)
    print_board(sample_board)


main()
