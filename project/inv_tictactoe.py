"""
Avoid-3 — Reverse Tic-Tac-Toe on a 4×4 Board
===========================================================
Includes both Vs Player and Vs AI modes.

Rules (inverted from classic Tic-Tac-Toe):

  INSTANT LOSS : If you form any 3 consecutive tiles
                 (row, column, or diagonal) you LOSE immediately.

  BOARD-FULL WIN: When no instant loss has occurred and the board
                  fills up, the player with the MOST unmatched tiles
                  (tiles NOT part of any 3-consecutive line) wins.

  DRAW         : Board fills, both players have equal unmatched tiles.
"""

import math


# Game Configuration


BOARD_SIZE         = 16    # 4×4 board
MAX_DEPTH          = 6     # depth limit for minimax
INSTANT_LOSS_SCORE = 100   # base score magnitude for 3-in-a-row terminal
BOARD_FULL_SCORE   = 50    # base score magnitude for unmatched-tile terminal

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


# Board Utilities


def create_board():
    return [" "] * BOARD_SIZE

def print_board(board):
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
    return [i for i, v in enumerate(board) if v == " "]


# Terminal State Detection


def has_instant_loss(board, player):
    for a, b, c in LOSS_LINES:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def count_unmatched(board, player):
    matched = set()
    for a, b, c in LOSS_LINES:
        if board[a] == board[b] == board[c] == player:
            matched.update([a, b, c])
    return sum(1 for i, v in enumerate(board) if v == player and i not in matched)

def check_terminal(board, last_player):
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

def is_terminal(board, last_player):
    return check_terminal(board, last_player) is not None


# Heuristic Evaluation & Minimax (AI Only)


def count_near_loss_lines(board, player):
    count = 0
    for a, b, c in LOSS_LINES:
        cells = [board[a], board[b], board[c]]
        if cells.count(player) == 2 and cells.count(" ") == 1:
            count += 1
    return count

def heuristic_score(board):
    ai_unmatched    = count_unmatched(board, "O")
    human_unmatched = count_unmatched(board, "X")
    ai_danger       = count_near_loss_lines(board, "O")
    human_danger    = count_near_loss_lines(board, "X")
    return (ai_unmatched - human_unmatched) + (human_danger - ai_danger) * 0.5

def minimax(board, depth, is_maximizing, last_player, alpha=-math.inf, beta=math.inf):
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
        return 0  

    if depth >= MAX_DEPTH:
        return heuristic_score(board)

    moves = get_available_moves(board)

    if is_maximizing:
        best = -math.inf
        for move in moves:
            board[move] = "O"
            score = minimax(board, depth + 1, False, "O", alpha, beta)
            board[move] = " "
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for move in moves:
            board[move] = "X"
            score = minimax(board, depth + 1, True, "X", alpha, beta)
            board[move] = " "
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

def best_ai_move(board):
    best_score = -math.inf
    best_move  = None
    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, 0, False, "O")
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move  = move
    return best_move


# Game Loop


def get_player_move(board, prompt):
    available = [str(m + 1) for m in get_available_moves(board)]
    while True:
        raw = input(f"  {prompt} (enter 1–16, available: {', '.join(available)}): ").strip()
        if raw in available:
            return int(raw) - 1
        print("  ✗ Invalid input. Please choose an available cell number.")

def decode_result(result, board, vs_ai):
    x_score = count_unmatched(board, "X")
    o_score = count_unmatched(board, "O")
    
    if vs_ai:
        score_line = f"  Unmatched tiles — You (X): {x_score}  |  AI (O): {o_score}"
        messages = {
            "X_LOSS": ("  ✗ You formed 3 in a row — YOU LOSE! ✗", score_line),
            "O_LOSS": ("  ★ AI formed 3 in a row — YOU WIN! ★",   score_line),
            "X_WIN":  ("  ★ You win! Most unmatched tiles. ★",     score_line),
            "O_WIN":  ("  ◉ AI wins! Most unmatched tiles. ◉",     score_line),
            "Draw":   ("  ══ It's a Draw! Equal unmatched tiles. ══", score_line),
        }
    else:
        score_line = f"  Unmatched tiles — Player X: {x_score}  |  Player O: {o_score}"
        messages = {
            "X_LOSS": ("  ✗ Player X formed 3 in a row — Player O WINS! ✗", score_line),
            "O_LOSS": ("  ✗ Player O formed 3 in a row — Player X WINS! ✗", score_line),
            "X_WIN":  ("  ★ Player X wins! Most unmatched tiles. ★",     score_line),
            "O_WIN":  ("  ★ Player O wins! Most unmatched tiles. ★",     score_line),
            "Draw":   ("  ══ It's a Draw! Equal unmatched tiles. ══", score_line),
        }
    return messages.get(result, ("  Game over.", score_line))

def play_game(vs_ai):
    print("=" * 52)
    mode_text = "Vs AI" if vs_ai else "2 Player"
    print(f"   AVOID-3  —  Reverse Tic-Tac-Toe on 4×4  ({mode_text})")
    print("=" * 52)
    if vs_ai:
        print("  You are X.  AI is O.  X goes first.\n")
    else:
        print("  Player 1 is X.  Player 2 is O.  X goes first.\n")
    print("  ⚠  Rules (REVERSED from classic Tic-Tac-Toe):")
    print("     • Forming 3 consecutive tiles = INSTANT LOSS")
    print("     • When board fills: most UNMATCHED tiles wins\n")

    board = create_board()
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            prompt = "Your move" if vs_ai else "Player X's move"
            move = get_player_move(board, prompt)
            board[move] = "X"
        else:
            if vs_ai:
                print("  AI is thinking…")
                move = best_ai_move(board)
                print(f"  AI placed O at position {move + 1}.")
            else:
                move = get_player_move(board, "Player O's move")
            board[move] = "O"

        result = check_terminal(board, current_player)
        if result is not None:
            print_board(board)
            msg, score_line = decode_result(result, board, vs_ai)
            print(msg)
            print(score_line)
            print()
            break

        current_player = "O" if current_player == "X" else "X"

def main():
    while True:
        print("===================================")
        print("       AVOID-3 MAIN MENU")
        print("===================================")
        print("1. Play vs AI")
        print("2. Play vs Human (2 Player)")
        print("3. Quit")
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            play_game(vs_ai=True)
            input("Press Enter to continue...")
        elif choice == '2':
            play_game(vs_ai=False)
            input("Press Enter to continue...")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
