import random

def create_board(size, num_mines):
    board = [['.' for _ in range(size)] for _ in range(size)]
    mines = set()
    while len(mines) < num_mines:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        mines.add((x, y))
    for x, y in mines:
        board[x][y] = '*'
    return board, mines

def display_board(board, revealed):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if revealed[i][j]:
                print(board[i][j], end=' ')
            else:
                print('?', end=' ')
        print()

def count_adjacent_mines(board, x, y):
    size = len(board)
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and board[nx][ny] == '*':
                count += 1
    return count

def play_game():
    size = 5
    num_mines = 5
    board, mines = create_board(size, num_mines)
    revealed = [[False for _ in range(size)] for _ in range(size)]
    
    while True:
        display_board(board, revealed)
        try:
            x, y = map(int, input("Enter coordinates (row col): ").split())
            if (x, y) in mines:
                print("Boom! You hit a mine. Game over!")
                break
            revealed[x][y] = True
            if board[x][y] == '.':
                board[x][y] = str(count_adjacent_mines(board, x, y))
            if all(revealed[i][j] or board[i][j] == '*' for i in range(size) for j in range(size)):
                print("Congratulations! You cleared the board!")
                break
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid coordinates.")

if __name__ == "__main__":
    play_game()