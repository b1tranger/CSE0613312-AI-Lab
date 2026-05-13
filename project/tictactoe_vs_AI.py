"""
Tic Tac Toe - 3x3 with Minimax Algorithm
=========================================
Classic Tic-Tac-Toe where:
  - 'X' always goes first (Human)
  - 'O' is the AI (uses Minimax to play optimally)
  - First player to get 3 in a row (row, col, or diagonal) wins.

Run:
    python tictactoe_minimax.py
"""

import math


# ─────────────────────────────────────────────────────────────
# Board utilities
# ─────────────────────────────────────────────────────────────

def create_board():
    """Return an empty 3x3 board represented as a list of 9 strings."""
    return [" "] * 9


def print_board(board):
    """Pretty-print the board with grid lines and position indices."""
    def cell(i):
        return board[i] if board[i] != " " else str(i + 1)

    print()
    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")
    print()


def get_available_moves(board):
    """Return indices of empty cells."""
    return [i for i, v in enumerate(board) if v == " "]


# ─────────────────────────────────────────────────────────────
# Win / Terminal state detection
# ─────────────────────────────────────────────────────────────

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]


def check_winner(board):
    """
    Return the winning player ('X' or 'O') if there is one,
    'Draw' if the board is full with no winner, else None.
    """
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if not get_available_moves(board):
        return "Draw"
    return None


def is_terminal(board):
    return check_winner(board) is not None


# ─────────────────────────────────────────────────────────────
# Minimax Algorithm
# ─────────────────────────────────────────────────────────────

def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    """
    Minimax with Alpha-Beta Pruning.

    Convention:
        Maximizing player → 'O' (AI)
        Minimizing player → 'X' (Human)

    Returns the best heuristic score for the current board state.

    Score:
        +10 - depth  →  AI wins  (prefer faster wins)
        -10 + depth  →  Human wins  (prefer slower losses)
        0            →  Draw
    """
    winner = check_winner(board)
    if winner == "O":
        return 10 - depth          # AI won
    if winner == "X":
        return depth - 10          # Human won
    if winner == "Draw":
        return 0                   # Draw

    moves = get_available_moves(board)

    if is_maximizing:             # AI's turn → maximise score
        best = -math.inf
        for move in moves:
            board[move] = "O"
            score = minimax(board, depth + 1, False, alpha, beta)
            board[move] = " "
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:
                break             # Beta cut-off
        return best
    else:                         # Human's turn → minimise score
        best = math.inf
        for move in moves:
            board[move] = "X"
            score = minimax(board, depth + 1, True, alpha, beta)
            board[move] = " "
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:
                break             # Alpha cut-off
        return best


def best_ai_move(board):
    """Evaluate all available moves and return the index with the best score."""
    best_score = -math.inf
    best_move = None

    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, 0, False)   # next turn is Human (minimizing)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move

    return best_move


# ─────────────────────────────────────────────────────────────
# Game Loop
# ─────────────────────────────────────────────────────────────

def get_human_move(board):
    """Prompt the human for a valid move (1-9) and return the 0-indexed cell."""
    available = [str(m + 1) for m in get_available_moves(board)]
    while True:
        raw = input(f"  Your move (choose from {', '.join(available)}): ").strip()
        if raw in available:
            return int(raw) - 1
        print("  ✗ Invalid input. Please enter an available cell number.")


def play_game():
    print("=" * 40)
    print("   TIC TAC TOE  —  Minimax AI (O)")
    print("=" * 40)
    print("  You are X.  AI is O.  X goes first.")
    print("  Enter a cell number (1-9) to place your mark.\n")
    print("  Cell layout:")
    print("   1 | 2 | 3 ")
    print("  ---+---+---")
    print("   4 | 5 | 6 ")
    print("  ---+---+---")
    print("   7 | 8 | 9 \n")

    board = create_board()
    current_player = "X"          # Human always goes first

    while True:
        print_board(board)

        if current_player == "X":
            move = get_human_move(board)
            board[move] = "X"
        else:
            print("  AI is thinking…")
            move = best_ai_move(board)
            board[move] = "O"
            print(f"  AI placed O at position {move + 1}.")

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "Draw":
                print("  ══ It's a Draw! ══\n")
            elif winner == "X":
                print("  ★ You win! Congratulations! ★\n")
            else:
                print("  ◉ AI wins! Better luck next time. ◉\n")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


# ─────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    while True:
        play_game()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye.\n")
            break
