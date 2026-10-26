
# ==========================================
# PROJECT 3: TIC-TAC-TOE AI USING MINIMAX
# ==========================================

import math

HUMAN = "X"
AI = "O"
EMPTY = " "


# ==========================================
# 1. CREATE THE BOARD
# ==========================================

def create_board():
    return [EMPTY] * 9


# ==========================================
# 2. DISPLAY THE BOARD
# ==========================================

def display_board(board):
    print()

    for row in range(3):
        start = row * 3

        print(
            f" {board[start]} | {board[start + 1]} | {board[start + 2]} "
        )

        if row < 2:
            print("---+---+---")

    print()


# ==========================================
# 3. CHECK WINNING CONDITIONS
# ==========================================

def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),  # First row
        (3, 4, 5),  # Second row
        (6, 7, 8),  # Third row
        (0, 3, 6),  # First column
        (1, 4, 7),  # Second column
        (2, 5, 8),  # Third column
        (0, 4, 8),  # Main diagonal
        (2, 4, 6)   # Other diagonal
    ]

    for a, b, c in winning_combinations:
        if (
            board[a] == player
            and board[b] == player
            and board[c] == player
        ):
            return True

    return False


# ==========================================
# 4. CHECK EMPTY POSITIONS
# ==========================================

def get_available_moves(board):
    return [
        i for i in range(9)
        if board[i] == EMPTY
    ]


# ==========================================
# 5. EVALUATE THE BOARD
# ==========================================

def evaluate(board):
    if check_winner(board, AI):
        return 1

    if check_winner(board, HUMAN):
        return -1

    return 0


# ==========================================
# 6. MINIMAX ALGORITHM
# ==========================================

def minimax(board, is_maximizing):
    score = evaluate(board)

    # Stop when a player wins or the game is drawn
    if score != 0:
        return score

    if not get_available_moves(board):
        return 0

    # AI tries to maximize the score
    if is_maximizing:
        best_score = -math.inf

        for move in get_available_moves(board):
            board[move] = AI

            score = minimax(board, False)

            board[move] = EMPTY

            best_score = max(best_score, score)

        return best_score

    # Human tries to minimize the score
    else:
        best_score = math.inf

        for move in get_available_moves(board):
            board[move] = HUMAN

            score = minimax(board, True)

            board[move] = EMPTY

            best_score = min(best_score, score)

        return best_score


# ==========================================
# 7. FIND THE BEST MOVE FOR THE AI
# ==========================================

def find_best_move(board):
    best_score = -math.inf
    best_move = None

    for move in get_available_moves(board):
        board[move] = AI

        score = minimax(board, False)

        board[move] = EMPTY

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


# ==========================================
# 8. HUMAN PLAYER
# ==========================================

def human_move(board):
    while True:
        try:
            move = int(input("Enter a position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Please enter a number from 1 to 9.")
            elif board[move] != EMPTY:
                print("That position is already occupied.")
            else:
                board[move] = HUMAN
                break

        except ValueError:
            print("Invalid input. Please enter a number.")


# ==========================================
# 9. MAIN GAME
# ==========================================

def main():
    board = create_board()

    print("=" * 35)
    print("       TIC-TAC-TOE AI")
    print("       Minimax Algorithm")
    print("=" * 35)

    print("\nYou are X. The AI is O.")
    print("Choose positions using numbers 1 to 9.")

    print("""
Position guide:

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
""")

    while True:
        # Human plays first
        human_move(board)
        display_board(board)

        if check_winner(board, HUMAN):
            print("Congratulations! You won!")
            break

        if not get_available_moves(board):
            print("The game is a draw!")
            break

        # AI chooses its best move
        print("AI is thinking...")

        move = find_best_move(board)

        if move is not None:
            board[move] = AI

        print(f"AI chooses position {move + 1}.")
        display_board(board)

        if check_winner(board, AI):
            print("AI wins! Better luck next time.")
            break

        if not get_available_moves(board):
            print("The game is a draw!")
            break


# ==========================================
# 10. START THE GAME
# ==========================================

if __name__ == "__main__":
    main()

