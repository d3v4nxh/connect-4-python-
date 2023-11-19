def print_board(board):
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n" + "-" * (7 * len(row) + 1))

def check_win(board, player):
    # Check horizontally
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check vertically
    for col in range(len(board[0])):
        if all(board[row][col] == player for row in range(len(board))):
            return True

    # Check diagonally (bottom-left to top-right)
    for row in range(3, len(board)):
        for col in range(len(board[0]) - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    # Check diagonally (top-left to bottom-right)
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    return False

def is_valid_move(board, col):
    return 0 <= col < len(board[0]) and board[0][col] == 0

def make_move(board, col, player):
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = player
            break

def connect_four():
    board = [[0] * 7 for _ in range(6)]
    players = [1, 2]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        col = int(input(f"Player {player}, choose a column (0-6): "))

        if is_valid_move(board, col):
            make_move(board, col, player)

            if check_win(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break

            if all(cell != 0 for row in board for cell in row):
                print_board(board)
                print("It's a draw!")
                break

            turn += 1
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    connect_four()
