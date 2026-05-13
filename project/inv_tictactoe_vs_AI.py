"""
Avoid-3 — Reverse Tic-Tac-Toe on a 4×4 Board (Minimax AI)
===========================================================
Rules (inverted from classic Tic-Tac-Toe):

  INSTANT LOSS : If you form any 3 consecutive tiles
                 (row, column, or diagonal) you LOSE immediately.

  BOARD-FULL WIN: When no instant loss has occurred and the board
                  fills up, the player with the MOST unmatched tiles
                  (tiles NOT part of any 3-consecutive line) wins.

  DRAW         : Board fills, both players have equal unmatched tiles.

Players:
  'X' → Human (goes first)
  'O' → AI    (uses depth-limited Minimax with Alpha-Beta Pruning)

Run:
    python avoid3_minimax.py
"""

import math

# ─────────────────────────────────────────────────────────────
# Game Configuration
# ─────────────────────────────────────────────────────────────

BOARD_SIZE         = 16    # 4×4 board
MAX_DEPTH          = 6     # depth limit for minimax (keeps AI responsive)
INSTANT_LOSS_SCORE = 100   # base score magnitude for 3-in-a-row terminal
BOARD_FULL_SCORE   = 50    # base score magnitude for unmatched-tile terminal

# 4×4 index layout:
#  0  |  1  |  2  |  3
#  4  |  5  |  6  |  7
#  8  |  9  | 10  | 11
# 12  | 13  | 14  | 15

# All 3-consecutive sequences on the 4×4 grid.
# Forming ANY of these with your own tiles → INSTANT LOSS.
LOSS_LINES = [
    # Rows (2 sliding windows per row × 4 rows)
    (0, 1, 2),   (1, 2, 3),
    (4, 5, 6),   (5, 6, 7),
    (8, 9, 10),  (9, 10, 11),
    (12, 13, 14),(13, 14, 15),
    # Columns (2 windows per column × 4 columns)
    (0, 4, 8),   (4, 8, 12),
    (1, 5, 9),   (5, 9, 13),
    (2, 6, 10),  (6, 10, 14),
    (3, 7, 11),  (7, 11, 15),
    # Diagonals ↘ (top-left → bottom-right, 4 windows)
    (0, 5, 10),  (1, 6, 11),
    (4, 9, 14),  (5, 10, 15),
    # Diagonals ↗ (top-right → bottom-left, 4 windows)
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
    This is an INSTANT LOSS condition for that player.
    """
    for a, b, c in LOSS_LINES:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def count_unmatched(board, player):
    """
    Count tiles owned by 'player' that are NOT part of any 3-consecutive line.
    These are the "unmatched" tiles that contribute to the player's score
    when the board fills without an instant loss.
    """
    matched = set()
    for a, b, c in LOSS_LINES:
        if board[a] == board[b] == board[c] == player:
            matched.update([a, b, c])
    return sum(1 for i, v in enumerate(board) if v == player and i not in matched)


def check_terminal(board, last_player):
    """
    Check whether the game has ended after 'last_player' just moved.

    Returns one of:
        'X_LOSS'  — X formed 3 in a row (X loses instantly)
        'O_LOSS'  — O formed 3 in a row (O loses instantly)
        'X_WIN'   — board full; X has more unmatched tiles
        'O_WIN'   — board full; O has more unmatched tiles
        'Draw'    — board full; equal unmatched tiles
        None      — game still in progress
    """
    # Step 1: Instant loss for the player who just moved
    if has_instant_loss(board, last_player):
        return f"{last_player}_LOSS"

    # Step 2: Board full → count unmatched tiles
    if not get_available_moves(board):
        x_score = count_unmatched(board, "X")
        o_score = count_unmatched(board, "O")
        if x_score > o_score:
            return "X_WIN"
        if o_score > x_score:
            return "O_WIN"
        return "Draw"

    # Step 3: Game continues
    return None


def is_terminal(board, last_player):
    """Return True if the game has ended."""
    return check_terminal(board, last_player) is not None


# ─────────────────────────────────────────────────────────────
# Heuristic Evaluation (for depth-limited search)
# ─────────────────────────────────────────────────────────────

def count_near_loss_lines(board, player):
    """
    Count LOSS_LINES that have exactly 2 tiles of 'player' and 1 empty cell.
    These represent positions one move away from an instant loss — high danger.
    """
    count = 0
    for a, b, c in LOSS_LINES:
        cells = [board[a], board[b], board[c]]
        if cells.count(player) == 2 and cells.count(" ") == 1:
            count += 1
    return count


def heuristic_score(board):
    """
    Estimate board value when search is cut off at MAX_DEPTH.

    AI = 'O' (maximizing). Positive score favours AI.

    Components:
      + (AI unmatched - Human unmatched)  : favour AI having more safe tiles
      + (Human danger - AI danger) × 0.5  : favour human being closer to
                                            instant loss, AI being safer
    """
    ai_unmatched    = count_unmatched(board, "O")
    human_unmatched = count_unmatched(board, "X")
    ai_danger       = count_near_loss_lines(board, "O")
    human_danger    = count_near_loss_lines(board, "X")
    return (ai_unmatched - human_unmatched) + (human_danger - ai_danger) * 0.5


# ─────────────────────────────────────────────────────────────
# Minimax with Alpha-Beta Pruning + Depth Limit
# ─────────────────────────────────────────────────────────────

def minimax(board, depth, is_maximizing, last_player,
            alpha=-math.inf, beta=math.inf):
    """
    Minimax with Alpha-Beta Pruning and a depth limit (MAX_DEPTH).

    Convention:
        Maximizing player → 'O' (AI)
        Minimizing player → 'X' (Human)

    Score table (from AI perspective):
        O_LOSS → -(INSTANT_LOSS_SCORE - depth)   AI loses fast → very bad
        X_LOSS → +(INSTANT_LOSS_SCORE - depth)   Human loses fast → very good
        O_WIN  → +(BOARD_FULL_SCORE  - depth)    AI wins → good
        X_WIN  → -(BOARD_FULL_SCORE  - depth)    Human wins → bad
        Draw   → 0

    Depth adjustment:
        For AI losses: prefer SLOWER losses (give opponent more chances to err)
        For AI wins:   prefer FASTER wins
    """
    result = check_terminal(board, last_player)
    if result is not None:
        if result == "O_LOSS":
            return -(INSTANT_LOSS_SCORE - depth)
        if result == "X_LOSS":
            return  (INSTANT_LOSS_SCORE - depth)
        if result == "O_WIN":
            return  (BOARD_FULL_SCORE   - depth)
        if result == "X_WIN":
            return -(BOARD_FULL_SCORE   - depth)
        return 0  # Draw

    # Depth cutoff → heuristic evaluation
    if depth >= MAX_DEPTH:
        return heuristic_score(board)

    moves = get_available_moves(board)

    if is_maximizing:         # AI ('O') tries to maximise score
        best = -math.inf
        for move in moves:
            board[move] = "O"
            score = minimax(board, depth + 1, False, "O", alpha, beta)
            board[move] = " "
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:
                break         # Beta cut-off
        return best
    else:                     # Human ('X') tries to minimise score
        best = math.inf
        for move in moves:
            board[move] = "X"
            score = minimax(board, depth + 1, True, "X", alpha, beta)
            board[move] = " "
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:
                break         # Alpha cut-off
        return best


def best_ai_move(board):
    """Evaluate all available moves and return the index with the best score for AI."""
    best_score = -math.inf
    best_move  = None

    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, 0, False, "O")   # AI just moved; human is next
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move  = move

    return best_move


# ─────────────────────────────────────────────────────────────
# Game Loop
# ─────────────────────────────────────────────────────────────

def get_human_move(board):
    """Prompt the human for a valid move (1-16) and return the 0-indexed cell."""
    available = [str(m + 1) for m in get_available_moves(board)]
    while True:
        raw = input(f"  Your move (enter 1–16, available: {', '.join(available)}): ").strip()
        if raw in available:
            return int(raw) - 1
        print("  ✗ Invalid input. Please choose an available cell number.")


def decode_result(result, board):
    """Return a user-friendly message and score line for a terminal result."""
    x_score = count_unmatched(board, "X")
    o_score = count_unmatched(board, "O")
    score_line = f"  Unmatched tiles — You (X): {x_score}  |  AI (O): {o_score}"

    messages = {
        "X_LOSS": ("  ✗ You formed 3 in a row — YOU LOSE! ✗", score_line),
        "O_LOSS": ("  ★ AI formed 3 in a row — YOU WIN! ★",   score_line),
        "X_WIN":  ("  ★ You win! Most unmatched tiles. ★",     score_line),
        "O_WIN":  ("  ◉ AI wins! Most unmatched tiles. ◉",     score_line),
        "Draw":   ("  ══ It's a Draw! Equal unmatched tiles. ══", score_line),
    }
    return messages.get(result, ("  Game over.", score_line))


def play_game():
    print("=" * 52)
    print("   AVOID-3  —  Reverse Tic-Tac-Toe on 4×4  (AI: O)")
    print("=" * 52)
    print("  You are X.  AI is O.  X goes first.\n")
    print("  ⚠  Rules (REVERSED from classic Tic-Tac-Toe):")
    print("     • Forming 3 consecutive tiles = INSTANT LOSS")
    print("     • When board fills: most UNMATCHED tiles wins\n")
    print("  Cell positions:")
    print("    1  |  2  |  3  |  4 ")
    print("  ----+-----+-----+----")
    print("    5  |  6  |  7  |  8 ")
    print("  ----+-----+-----+----")
    print("    9  | 10  | 11  | 12 ")
    print("  ----+-----+-----+----")
    print("   13  | 14  | 15  | 16 \n")

    board = create_board()
    current_player = "X"    # Human always goes first

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

        result = check_terminal(board, current_player)
        if result is not None:
            print_board(board)
            msg, score_line = decode_result(result, board)
            print(msg)
            print(score_line)
            print()
            break

        current_player = "O" if current_player == "X" else "X"


# ─────────────────────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    while True:
        play_game()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye.\n")
            break
