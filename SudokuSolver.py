import time

# prints the sudoku board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("--------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end = "")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")

# find empty spaces on board
def nextCellToFill(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return (-1,-1)

# determine if the number is valid for that specific position
def valid(board, position, number):

    # row
    for i in range(len(board[0])):
        if board[position[0]][i] == number:
            return False
    # column
    for i in range(len(board)):
        if board[i][position[1]] == number:
            return False

    # boxes
    x_box = position[1] // 3
    y_box = position[0] // 3

    for i in range(y_box * 3, y_box * 3 + 3):
        for j in range(x_box * 3, x_box * 3 + 3):
            if board[i][j] == number:
                return False

    return True

def solve(board):
    row, column = nextCellToFill(board)
    if row == -1:
        return True

    for i in range(1, 10):
        if valid(board, (row, column), i):
            board[row][column] = i

            # recursively call solve again until no more empty cells to fill
            if solve(board):
                return True

            # backtracking method such that if solve returns false, a 0 gets placed in that specific row and column
            board[row][column] = 0

    return False

def main():
    board = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]

    print_board(board)
    start_time = time.time()
    solve(board)
    end_time = time.time()
    print("\n")
    print("Solved Board:")
    print_board(board)
    print("The solver has taken", end_time - start_time, "seconds to solve.")

if __name__ == "__main__":
    main()