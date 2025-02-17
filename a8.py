Lab 4:  AI- Two Player Game

Python implementation of the Connect Four game for two players. Connect Four is a two-player board game where players take turns dropping colored discs into a grid, with the goal of getting four discs in a row either horizontally, vertically, or diagonally.
Question 1: Connect Four :Game Implementation
The implementation will include:
A function to initialize the game board.
Functions to display the board, make moves, and check for a win.
The main game loop for players to take turns.
How It Works:
Board Initialization: The board is initialized as a 6x7 grid of zeros (representing empty spaces).
Player Moves: Players take turns making moves by specifying a column. The discs fall to the lowest available position in the chosen column.
Win Check: After each move, the board is checked for a winning condition: four consecutive discs horizontally, vertically, or diagonally.
Game Loop: The game continues until a player wins or the board is full, resulting in a draw.
To run this code, simply copy and paste it into a Python environment and execute it. The game will prompt players to input their moves and display the board after each move.
Python Code
------ ------------------ --------------------- --------------------------------------------------
import numpy as np

# Constants
ROWS = 6
COLS = 7
EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2

def create_board():
    return np.zeros((ROWS, COLS), dtype=int)

def print_board(board):
    print(np.flip(board, 0))

def is_valid_move(board, col):
    return board[ROWS-1][col] == EMPTY

def make_move(board, col, player):
    for row in range(ROWS):
        if board[row][col] == EMPTY:
            board[row][col] = player
            break

def check_winner(board, player):
    # Check horizontal, vertical, and diagonal lines
    for c in range(COLS - 3):
        for r in range(ROWS):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return True

    for c in range(COLS):
        for r in range(ROWS - 3):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True

    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True

    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True

    return False

def main():
    board = create_board()
    game_over = False
    turn = PLAYER1

    while not game_over:
        print_board(board)
        col = int(input(f"Player {turn}, make your move (0-{COLS-1}): "))

        if col < 0 or col >= COLS:
            print("Invalid column. Try again.")
            continue

        if not is_valid_move(board, col):
            print("Column full. Try another column.")
            continue

        make_move(board, col, turn)

        if check_winner(board, turn):
            print_board(board)
            print(f"Player {turn} wins!")
            game_over = True
        else:
            if np.all(board != EMPTY):
                print_board(board)
                print("The game is a draw!")
                game_over = True
            else:
                turn = PLAYER2 if turn == PLAYER1 else PLAYER1

if __name__ == "__main__":
    main()
----   -----------------------   ------------------------
What are the bugs in the above code (if any)?
Run the code  and submit the result for different number of row total, and different no of column total
Execute the code so that Player 1= You roll no; Player 2= Player 1-100
Convert the Four connect game to Five connect game
Highlight the code byte which verifies the winning condition

Modify the code so that initial stages of unnecessary search/verification of winning conditions is eliminated
Modify the code so that total number of row, column, and winning count are taken from user; and it is ensured that at least one of the total count of row and column becomes greater than winning count

Question 2
N Queen Problem
Below is a Python implementation of the N-Queens problem, where the user can specify the value of N. The goal is to place N queens on an N x N chessboard such that no two queens threaten each other (i.e., no two queens share the same row, column, or diagonal).
def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, N, solutions):
    # If all queens are placed, add the solution to the list
    if col >= N:
        solutions.append(["".join("Q" if board[i][j] == 1 else "." for j in range(N)) for i in range(N)])
        return

    # Consider this column and try placing the queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_n_queens_util(board, col + 1, N, solutions)

            # Backtrack and remove the queen
            board[i][col] = 0

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions

def print_solutions(solutions):
    for idx, solution in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in solution:
            print(row)
        print("")

# Example usage
N = int(input("Enter the value of N for the N-Queens problem: "))
solutions = solve_n_queens(N)

if solutions:
    print(f"Total solutions for {N}-Queens problem: {len(solutions)}")
    print_solutions(solutions)
else:
    print(f"No solutions exist for {N}-Queens problem.")
-----------   -------------------------   -------------------------   ------------
What are the bugs in the above code (if any)?
Run the code  and submit the result for different number of N
Make changes to the code so that results Mark Queen as Qn
Which line is controlling the board size in the above problem
What is the role of zip(range….)?

Make the changes in the code so that Queen size becomes N however Board size become M where M>N; code allows to set N, M and run successfully to results; How you had changed the given cod eto achieve this?
Problem 3
Sudoku solution
def is_valid(board, row, col, num):
    # Check if num is not in the current row
    if num in board[row]:
        return False

    # Check if num is not in the current column
    for i in range(4):
        if board[i][col] == num:
            return False

    # Check if num is not in the current 2x2 sub-grid
    start_row = row - row % 2
    start_col = col - col % 2
    for i in range(2):
        for j in range(2):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    # Find the next empty cell
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                # Try each number from 1 to 4
                for num in range(1, 5):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        # Recursively attempt to solve the rest of the board
                        if solve_sudoku(board):
                            return True

                        # If placing num doesn't lead to a solution, backtrack
                        board[row][col] = 0

                return False

    # All cells are filled, solution found
    return True

def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

# Example 4x4 Sudoku board with some numbers filled in
board = [
    [1, 0, 0, 4],
    [0, 0, 3, 0],
    [0, 4, 0, 0],
    [0, 0, 0, 2]
]

if solve_sudoku(board):
    print("Sudoku solved successfully!")
    print_board(board)
else:
    print("No solution exists.")
----------------                    ----------------------------                  --------------------
What are the bugs in the above code (if any)?
Run the code  for three different initial settings
Make changes to the code so 1,2,3,4 are modified as your roll no functions
Can you change it to 5X5 sudoku
What are the constraints satisfied in this sudoku. Can you suggest cases where 2x2 constraint is not satisfied 
What is the role of zip(range….)?
Question 4
Tic tac toe
import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if there are any available moves left
def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

# Function to evaluate the board
def evaluate(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return 10 if row[0] == 'X' else -10

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return 10 if board[0][col] == 'X' else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return 10 if board[0][0] == 'X' else -10
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return 10 if board[0][2] == 'X' else -10

    # If no winner, return 0
    return 0

# Minimax function to find the best move for the computer
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 10:
        return score - depth  # Prefer winning earlier
    if score == -10:
        return score + depth  # Prefer opponent losing later

    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = ' '
        return best

# Function to find the best move for the computer
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Function to check if there is a winner or the game is a draw
def check_game_over(board):
    score = evaluate(board)
    if score == 10:
        print("X wins!")
        return True
    if score == -10:
        print("O wins!")
        return True
    if not is_moves_left(board):
        print("It's a draw!")
        return True
    return False

# Main function to run the Tic-Tac-Toe game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if row not in range(3) or col not in range(3):
                print("Invalid move. Row and column must be between 0 and 2. Try again.")
                continue
            if board[row][col] != ' ':
                print("Invalid move. Cell already occupied. Try again.")
                continue
            board[row][col] = 'O'
            print_board(board)
            if check_game_over(board):
                break

            print("Computer's turn:")
            x, y = find_best_move(board)
            board[x][y] = 'X'
            print_board(board)
            if check_game_over(board):
                break
        except ValueError:
            print("Invalid input. Please enter row and column as two integers separated by a space. Try again.")

play_game()
--------------   -------------------------------   ---------------------------
Modified Tic Tac toe
-----------------------------------------
import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if there are any available moves left
def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

# Function to evaluate the board
def evaluate(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return 10 if row[0] == 'X' else -10

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return 10 if board[0][col] == 'X' else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return 10 if board[0][0] == 'X' else -10
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return 10 if board[0][2] == 'X' else -10

    # If no winner, return 0
    return 0

# Minimax function to find the best move for the computer
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 10:
        return score - depth  # Prefer winning earlier
    if score == -10:
        return score + depth  # Prefer opponent losing later

    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = ' '
        return best

# Function to evaluate all possible moves and provide guidance
def evaluate_moves(board):
    guidance = []
    for i in range(3):
        row_guidance = []
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, True)
                board[i][j] = ' '
                if move_val == -10:
                    row_guidance.append("Win")
                elif move_val == 0:
                    row_guidance.append("Draw")
                else:
                    row_guidance.append("Lose")
            else:
                row_guidance.append("N/A")
        guidance.append(row_guidance)
    
    print("\nGuidance for each position (Win/Draw/Lose):")
    for row in guidance:
        print(" | ".join(row))
        print("-" * 17)

# Function to check if there is a winner or the game is a draw
def check_game_over(board):
    score = evaluate(board)
    if score == 10:
        print("X wins!")
        return True
    if score == -10:
        print("O wins!")
        return True
    if not is_moves_left(board):
        print("It's a draw!")
        return True
    return False

# Main function to run the Tic-Tac-Toe game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        evaluate_moves(board)  # Provide guidance before each move
        
        try:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if row not in range(3) or col not in range(3):
                print("Invalid move. Row and column must be between 0 and 2. Try again.")
                continue
            if board[row][col] != ' ':
                print("Invalid move. Cell already occupied. Try again.")
                continue
            board[row][col] = 'O'
            print_board(board)
            if check_game_over(board):
                break

            print("Computer's turn:")
            x, y = find_best_move(board)
            board[x][y] = 'X'
            print_board(board)
            if check_game_over(board):
                break
        except ValueError:
            print("Invalid input. Please enter row and column as two integers separated by a space. Try again.")

# Function to find the best move for the computer
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

play_game()
----------------------    -----------------------   ---------------------
Compare Tic tac toe and modified tic tac toe for three different random beginning.     How are they different
Can you change X and O sign
Can you modify board size
What are the bugs in above code
Question 5
Write a two heap NIP game; show its execution
