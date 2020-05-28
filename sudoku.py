import time
sample_board = [
        [7, 8, " ", 4, " ", " ", 1, 2, " "],
        [6, " ", " ", " ", 7, 5, " ", " ", 9],
        [" ", " ", " ", 6, " ", 1, " ", 7, 8],
        [" ", " ", 7, " ", 4, " ", 2, 6, " "],
        [" ", " ", 1, " ", 5, " ", 9, 3, " "],
        [9, " ", 4, " ", 6, " ", " ", " ", 5],
        [" ", 7, " ", 3, " ", " ", " ", 1, 2],
        [1, 2, " ", " ", " ", 7, 4, " ", " "],
        [" ", 4, 9, 2, " ", 6, " ", " ", 7]
]

def solve(bo):
    """
    Solves a sudoku puzzle using backtracking
    :param bo: 2d list of ints
    :return: solution
    """
    find = find_empty(bo)
    if not find:
        return True # solved if no empty squares
    else:
        row, col = find # locate coordinates of empty square
        
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i # if is it a valid number

            if solve(bo):
                return True # solved if now no empty squares

            bo[row][col] = " " # backtrack
            
    return False

def find_empty(bo):
    """
    Finds an empty space in the board
    :param bo: partially complete board
    :return: (int, int) row col
    """
    for i in range(len(bo)): # loop over row
        for j in range(len(bo[0])): # loop over col
            if bo[i][j] == " ":
                return (i, j)  # row, col
                
    return None

def valid(bo, num, pos):
    """
    Returns if the attempted move is valid
    :param bo: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """
    # check for duplicates in row
    for i in range(9):
        if bo[pos[0]][i] == num:
            return False
    # check for duplicates in column
    for i in range(9):
        if bo[i][pos[1]] == num:
            return False

    # check for duplicates in box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num:
                return False

    return True

def print_board(bo):
    """
    Prints the board
    :param bo: 2d list of lists
    :return: None
    """
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
                
def execute():
    """
    Executes whole solving process
    :return: None
    """
    print("SUDOKU PUZZLE...")
    print_board(sample_board)
    print(" \nSOLVING PUZZLE...SOLVED!")
    start_time = time.time() # start timer
    solve(sample_board)
    end_time = time.time() - start_time # end timer
    print_board(sample_board)
    print(" \nTime used:", end_time, "seconds")
    
execute()
