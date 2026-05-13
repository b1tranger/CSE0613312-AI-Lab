"""
Tic Tac Toe — 2 Player (Human vs Human)
========================================
Classic 3×3 Tic-Tac-Toe for two players on the same machine.

Rules:
  • Player 1 uses 'X', Player 2 uses 'O'
  • Players alternate turns
  • First to get 3 in a row (row, column, or diagonal) wins
  • Board fills with no winner → Draw

Run:
    python tictactoe_2player.py
"""


# ─────────────────────────────────────────────────────────────
# Board Utilities
# ─────────────────────────────────────────────────────────────

def create_board():
    """Return an empty 3×3 board as a list of 9 single-space strings."""
    return [" "] * 9


def print_board(board):
    """
    Display the board with grid lines.
    Empty cells show their position number (1–9) as a hint.
    """
    def cell(i):
        return board[i] if board[i] != " " else str(i + 1)

    print()
    print(f"  {cell(0)} | {cell(1)} | {cell(2)} ")
    print(" ---+---+---")
    print(f"  {cell(3)} | {cell(4)} | {cell(5)} ")
    print(" ---+---+---")
    print(f"  {cell(6)} | {cell(7)} | {cell(8)} ")
    print()


def get_available_moves(board):
    """Return a list of indices for all empty (available) cells."""
    return [i for i, v in enumerate(board) if v == " "]


# ─────────────────────────────────────────────────────────────
# Win / Terminal State Detection
# ─────────────────────────────────────────────────────────────

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]


def check_winner(board):
    """
    Scan all 8 possible winning lines.

    Returns:
        'X'    — Player 1 has 3 in a row
        'O'    — Player 2 has 3 in a row
        'Draw' — board is full with no winner
        None   — game is still in progress
    """
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]             # winner symbol ('X' or 'O')

    if not get_available_moves(board):  # no moves left
        return "Draw"

    return None                         # game continues


# ─────────────────────────────────────────────────────────────
# Input Handling
# ─────────────────────────────────────────────────────────────

def get_player_move(board, player_name, symbol):
    """
    Prompt the active player for a valid cell number (1–9).

    Args:
        board       — current board state
        player_name — display name, e.g. 'Player 1'
        symbol      — 'X' or 'O'

    Returns:
        Zero-based index of the chosen cell.
    """
    available = [str(m + 1) for m in get_available_moves(board)]
    while True:
        raw = input(f"  {player_name} ({symbol}), choose a cell "
                    f"[{', '.join(available)}]: ").strip()
        if raw in available:
            return int(raw) - 1
        print(f"  ✗ '{raw}' is not valid. Please choose an available cell.")


# ─────────────────────────────────────────────────────────────
# Score Tracking
# ─────────────────────────────────────────────────────────────

def print_scores(scores, names):
    """Print the running score for both players and draws."""
    print(f"  ┌─ Score ──────────────────────────────┐")
    print(f"  │  {names[0]} (X): {scores['X']:<4} "
          f" {names[1]} (O): {scores['O']:<4} Draws: {scores['Draw']} │")
    print(f"  └──────────────────────────────────────┘")


# ─────────────────────────────────────────────────────────────
# Single Game
# ─────────────────────────────────────────────────────────────

def play_round(names):
    """
    Run one full round of Tic-Tac-Toe between two human players.

    Args:
        names — tuple/list of two player name strings, e.g. ('Alice', 'Bob')

    Returns:
        'X', 'O', or 'Draw' indicating the round result.
    """
    board = create_board()

    # Map symbol → player name for easy lookup
    players = {
        "X": {"name": names[0], "symbol": "X"},
        "O": {"name": names[1], "symbol": "O"},
    }
    turn_order = ["X", "O"]     # X always starts first
    turn_index = 0

    while True:
        symbol = turn_order[turn_index % 2]
        player = players[symbol]

        print_board(board)
        print(f"  ── {player['name']}'s turn ──")

        move = get_player_move(board, player["name"], symbol)
        board[move] = symbol

        result = check_winner(board)
        if result is not None:
            print_board(board)
            if result == "Draw":
                print("  ══ It's a Draw! ══\n")
            else:
                winner_name = players[result]["name"]
                print(f"  ★ {winner_name} ({result}) wins! Congratulations! ★\n")
            return result

        turn_index += 1


# ─────────────────────────────────────────────────────────────
# Main Game Session (with score tracking)
# ─────────────────────────────────────────────────────────────

def main():
    print("=" * 44)
    print("   TIC TAC TOE  —  2 Player Mode")
    print("=" * 44)
    print("  Cell positions for reference:")
    print("   1 | 2 | 3 ")
    print("  ---+---+---")
    print("   4 | 5 | 6 ")
    print("  ---+---+---")
    print("   7 | 8 | 9 \n")

    # Ask for player names
    p1 = input("  Enter name for Player 1 (X) [default: Player 1]: ").strip()
    p2 = input("  Enter name for Player 2 (O) [default: Player 2]: ").strip()
    p1 = p1 if p1 else "Player 1"
    p2 = p2 if p2 else "Player 2"
    names = (p1, p2)

    scores = {"X": 0, "O": 0, "Draw": 0}

    while True:
        print()
        print_scores(scores, names)
        print()

        result = play_round(names)

        # Update score
        scores[result] += 1
        print_scores(scores, names)

        again = input("\n  Play another round? (y/n): ").strip().lower()
        if again != "y":
            print(f"\n  Final Score:")
            print(f"    {p1} (X): {scores['X']} wins")
            print(f"    {p2} (O): {scores['O']} wins")
            print(f"    Draws:   {scores['Draw']}")
            print(f"\n  Thanks for playing! Goodbye.\n")
            break


# ─────────────────────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
