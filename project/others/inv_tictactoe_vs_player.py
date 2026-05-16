"""
Avoid-3 — Reverse Tic-Tac-Toe on a 4×4 Board (2 Player)
===========================================================
Rules (inverted from classic Tic-Tac-Toe):

  INSTANT LOSS : If you form any 3 consecutive tiles
                 (row, column, or diagonal) you LOSE immediately.

  BOARD-FULL WIN: When no instant loss has occurred and the board
                  fills up, the player with the MOST unmatched tiles
                  (tiles NOT part of any 3-consecutive line) wins.

  DRAW         : Board fills, both players have equal unmatched tiles.

Players:
  'X' → Player 1 (goes first)
  'O' → Player 2

Run:
    python inv_tictactoe_vs_player.py
"""

# ─────────────────────────────────────────────────────────────
# Game Configuration
# ─────────────────────────────────────────────────────────────

BOARD_SIZE = 16    # 4×4 board

# All 3-consecutive sequences on the 4×4 grid.
# Forming ANY of these with your own tiles → INSTANT LOSS.
LOSS_LINES = [
    # Rows
    (0, 1, 2),   (1, 2, 3),
    (4, 5, 6),   (5, 6, 7),
    (8, 9, 10),  (9, 10, 11),
    (12, 13, 14),(13, 14, 15),
    # Columns
    (0, 4, 8),   (4, 8, 12),
    (1, 5, 9),   (5, 9, 13),
    (2, 6, 10),  (6, 10, 14),
    (3, 7, 11),  (7, 11, 15),
    # Diagonals ↘
    (0, 5, 10),  (1, 6, 11),
    (4, 9, 14),  (5, 10, 15),
    # Diagonals ↗
    (2, 5, 8),   (3, 6, 9),
    (6, 9, 12),  (7, 10, 13),
]


# ─────────────────────────────────────────────────────────────
# Board Utilities
# ─────────────────────────────────────────────────────────────

def create_board():
    """Return an empty 4×4 board as a list of 16 strings."""
    return [" "] * BOARD_SIZE


def print_board(board):
    """Pretty-print the 4×4 board with cell position numbers for empty cells."""
    def cell(i):
        return f"{board[i]:^3}" if board[i] != " " else f"{i + 1:^3}"

    sep = "----+----+----+----"
    print()
    print(f" {cell(0)}| {cell(1)}| {cell(2)}| {cell(3)}")
    print(sep)
    print(f" {cell(4)}| {cell(5)}| {cell(6)}| {cell(7)}")
    print(sep)
    print(f" {cell(8)}| {cell(9)}| {cell(10)}| {cell(11)}")
    print(sep)
    print(f" {cell(12)}| {cell(13)}| {cell(14)}| {cell(15)}")
    print()


def get_available_moves(board):
    """Return list of empty cell indices."""
    return [i for i, v in enumerate(board) if v == " "]


# ─────────────────────────────────────────────────────────────
# Terminal State Detection
# ─────────────────────────────────────────────────────────────

def has_instant_loss(board, player):
    """
    Return True if 'player' has formed any 3-consecutive line on the board.
    """
    for a, b, c in LOSS_LINES:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def count_unmatched(board, player):
    """
    Count tiles owned by 'player' that are NOT part of any 3-consecutive line.
    """
    matched = set()
    for a, b, c in LOSS_LINES:
        if board[a] == board[b] == board[c] == player:
            matched.update([a, b, c])
    return sum(1 for i, v in enumerate(board) if v == player and i not in matched)


def check_terminal(board, last_player):
    """
    Check whether the game has ended after 'last_player' just moved.
    """
    if has_instant_loss(board, last_player):
        return f"{last_player}_LOSS"

    if not get_available_moves(board):
        x_score = count_unmatched(board, "X")
        o_score = count_unmatched(board, "O")
        if x_score > o_score:
            return "X_WIN"
        if o_score > x_score:
            return "O_WIN"
        return "Draw"

    return None


# ─────────────────────────────────────────────────────────────
# Game Loop
# ─────────────────────────────────────────────────────────────

def get_player_move(board, player):
    """Prompt the human player for a valid move (1-16)."""
    available = [str(m + 1) for m in get_available_moves(board)]
    while True:
        raw = input(f"  Player {player}'s move (enter 1–16, available: {', '.join(available)}): ").strip()
        if raw in available:
            return int(raw) - 1
        print("  ✗ Invalid input. Please choose an available cell number.")


def decode_result(result, board):
    """Return a user-friendly message and score line for a terminal result."""
    x_score = count_unmatched(board, "X")
    o_score = count_unmatched(board, "O")
    score_line = f"  Unmatched tiles — Player X: {x_score}  |  Player O: {o_score}"

    messages = {
        "X_LOSS": ("  ✗ Player X formed 3 in a row — Player O WINS! ✗", score_line),
        "O_LOSS": ("  ✗ Player O formed 3 in a row — Player X WINS! ✗", score_line),
        "X_WIN":  ("  ★ Player X wins! Most unmatched tiles. ★",     score_line),
        "O_WIN":  ("  ★ Player O wins! Most unmatched tiles. ★",     score_line),
        "Draw":   ("  ══ It's a Draw! Equal unmatched tiles. ══", score_line),
    }
    return messages.get(result, ("  Game over.", score_line))


def play_game():
    print("=" * 52)
    print("   AVOID-3  —  Reverse Tic-Tac-Toe on 4×4  (2 Player)")
    print("=" * 52)
    print("  Player 1 is X.  Player 2 is O.  X goes first.\n")
    print("  ⚠  Rules (REVERSED from classic Tic-Tac-Toe):")
    print("     • Forming 3 consecutive tiles = INSTANT LOSS")
    print("     • When board fills: most UNMATCHED tiles wins\n")

    board = create_board()
    current_player = "X"

    while True:
        print_board(board)

        move = get_player_move(board, current_player)
        board[move] = current_player

        result = check_terminal(board, current_player)
        if result is not None:
            print_board(board)
            msg, score_line = decode_result(result, board)
            print(msg)
            print(score_line)
            print()
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    while True:
        play_game()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye.\n")
            break
