# noughtsandcrosses.py

import random
import os.path
import json
random.seed()

def draw_board(board):
    # Draw the game board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    pass

def welcome(board):
    # Print a welcome message and display the initial board layout
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print("The Board Layout is shown below:")
    draw_board(board)
    pass

def initialise_board(board):
    # Set up the game board with empty cells
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    # Get the player's move
    while True:
        try:
            move = int(input("Enter the cell number (1-9): "))
            row = (move - 1) // 3
            col = (move - 1) % 3
            if 1 <= move <= 9 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_computer_move(board):
    # Simple implementation: choose a random empty cell
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)

def check_for_win(board, mark):
    # Check if a player has won
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)) or all(board[j][i] == mark for j in range(3)):
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def check_for_draw(board):
    # Check if the game is a draw
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def play_game(board):
    # Main game loop
    initialise_board(board)
    
    while True:
        # Player's turn
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = 'X'
        draw_board(board)

        # Check for player win or draw
        if check_for_win(board, 'X'):
            return 1
        elif check_for_draw(board):
            return 0

        # Computer's turn
        print("Computer_move")
        computer_row, computer_col = choose_computer_move(board)
        board[computer_row][computer_col] = 'O'
        draw_board(board)

        # Check for computer win or draw
        if check_for_win(board, 'O'):
            return -1
        elif check_for_draw(board):
            return 0

def menu():
    # Display menu options
    print("1 - Start Game")
    print("2 - Save score in 'leaderboard.txt'")
    print("3 - View Scores")
    print("q - End Game")
    return input("Enter your choice: ")

def load_scores():
    # Load scores from the leaderboard file
    if os.path.isfile('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as file:
            try:
                leaders = json.load(file)
            except json.JSONDecodeError:
                print("Error decoding leaderboard file. Creating a new one.")
                leaders = {}
    else:
        print("Leaderboard file not found. Creating a new one.")
        leaders = {}
    
    return leaders

def save_score(score):
    # Save the player's score to the leaderboard file
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open('leaderboard.txt', 'w') as file:
        json.dump(leaders, file)
    print(f"Score {score} saved for {name}.")

def display_leaderboard(leaders):
    # Display the leaderboard
    print("Leaderboard:")
    for name, score in leaders.items():
        print(f"{name}: {score}")
    pass
