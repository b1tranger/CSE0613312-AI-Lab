# Implementation Plan: Reverse Tic-Tac-Toe on a 4×4 Board

## Game Concept Summary

| Aspect | Classic TTT | New Game ("Avoid-3") |
|---|---|---|
| Board | 3×3 | 4×4 |
| Win condition | 3 in a row | Most **unmatched** tiles when board fills |
| Lose condition | Opponent gets 3 in a row | **You** get 3 in a row (instant loss) |
| Draw | Board full, no winner | Tied unmatched tile count at end |

---

## Section 1 — Conceptual Rule Changes

### 1.1 Understanding "Unmatched Tiles"

An **unmatched tile** is any cell you own that is **not part of any 3-consecutive sequence** (row, column, or diagonal — diagonals of length ≥ 3 count).

```
Example 4x4 board at game end:

  X | O | X | O
  O | X | O | X
  X | O | X | O
  O | X | O | X

No 3-in-a-row exists for either player.
X has 8 tiles, O has 8 tiles.
Count unmatched tiles per player → tiebreaker needed.
```

```
Example with an instant loss:

  X | X | X | O      ← X has 3 in a row (columns 0,1,2) → X loses INSTANTLY
  O | O | X | O
  ...
```

### 1.2 Matched vs Unmatched Tile Logic

A tile is **matched** (penalized) if it belongs to **at least one** 3-consecutive line:

```
Tile classification pseudocode:

for each cell owned by player P:
    for each WIN_LINE containing that cell:
        if all 3 cells in WIN_LINE belong to P:
            mark cell as "matched" (and trigger instant loss)
    if cell not in any matched line:
        count as "unmatched" → contributes to score
```

### 1.3 Scoring Philosophy (for Minimax)

```
Instant loss (3 in a row formed):
    Triggered immediately after placement, before opponent moves.
    Score = very negative for the player who formed it.

Terminal state (board full, no instant loss triggered):
    Score = (AI unmatched tiles) - (Human unmatched tiles)
    Positive → AI is winning
    Negative → Human is winning
    Zero → Draw
```

---

## Section 2 — Architectural Changes

### 2.1 Board Representation

```
Current (3×3):          New (4×4):
list of 9 strings       list of 16 strings

Index layout 3×3:       Index layout 4×4:
 0 | 1 | 2              0  | 1  | 2  | 3
 3 | 4 | 5              4  | 5  | 6  | 7
 6 | 7 | 8              8  | 9  | 10 | 11
                        12 | 13 | 14 | 15
```

**Change required:** `create_board()` returns `[" "] * 16`

### 2.2 Win Lines — All 3-Consecutive Sequences on 4×4

On a 4×4 grid, 3-in-a-row lines (not 4) include:

```
Rows (3 consecutive per row, 2 windows per row, 4 rows = 8 lines):
  Row 0: (0,1,2), (1,2,3)
  Row 1: (4,5,6), (5,6,7)
  Row 2: (8,9,10), (9,10,11)
  Row 3: (12,13,14), (13,14,15)

Columns (3 consecutive per col, 2 windows per col, 4 cols = 8 lines):
  Col 0: (0,4,8), (4,8,12)
  Col 1: (1,5,9), (5,9,13)
  Col 2: (2,6,10), (6,10,14)
  Col 3: (3,7,11), (7,11,15)

Diagonals ↘ (top-left to bottom-right, 3-length windows):
  (0,5,10), (1,6,11)
  (4,9,14), (5,10,15)
  (0,5,10) already listed — be careful of duplicates
  Systematically: start (r,c), go to (r+1,c+1), (r+2,c+2)
    Valid starts: r∈{0,1}, c∈{0,1} → 4 diagonals

Diagonals ↗ (top-right to bottom-left):
  start (r,c), go to (r+1,c-1), (r+2,c-2)
  Valid starts: r∈{0,1}, c∈{2,3} → 4 diagonals
```

Full enumeration:

```python
LOSS_LINES = [
    # Rows
    (0,1,2),(1,2,3),
    (4,5,6),(5,6,7),
    (8,9,10),(9,10,11),
    (12,13,14),(13,14,15),
    # Columns
    (0,4,8),(4,8,12),
    (1,5,9),(5,9,13),
    (2,6,10),(6,10,14),
    (3,7,11),(7,11,15),
    # Diagonals ↘
    (0,5,10),(1,6,11),
    (4,9,14),(5,10,15),
    # Diagonals ↗
    (2,5,8),(3,6,9),
    (6,9,12),(7,10,13),
]
```

---

## Section 3 — Function-by-Function Modification Plan

### 3.1 `create_board()`

```
CHANGE: Size 9 → 16

Before:  return [" "] * 9
After:   return [" "] * 16
```

### 3.2 `print_board()`

```
CHANGE: 3×3 ASCII grid → 4×4 ASCII grid

Before:
  cell indices 0-8, display rows of 3

After:
  cell indices 0-15, display rows of 4
  Use two-character width for numbers (1-16) for alignment

Visual template:
   1  |  2  |  3  |  4
  ----+-----+-----+----
   5  |  6  |  7  |  8
  ----+-----+-----+----
   9  | 10  | 11  | 12
  ----+-----+-----+----
  13  | 14  | 15  | 16
```

### 3.3 `get_available_moves()` — NO CHANGE NEEDED

```
Logic is index-agnostic, works for any board size.
No modification required.
```

### 3.4 `WIN_LINES` → Rename and Replace with `LOSS_LINES`

```
CHANGE: Rename constant, replace 3×3 win lines with
        ALL 3-consecutive sequences on 4×4 board.

Reason for rename: These lines now represent LOSING conditions,
                   not winning ones. Semantic clarity matters.
```

### 3.5 NEW FUNCTION: `has_instant_loss(board, player)`

```
PURPOSE:
  Check if 'player' has formed any 3-in-a-row → instant loss.

LOGIC:
  for each line in LOSS_LINES:
      if board[a] == board[b] == board[c] == player:
          return True
  return False

CALLED:
  Immediately after every move placement (both human and AI).
```

### 3.6 NEW FUNCTION: `count_unmatched(board, player)`

```
PURPOSE:
  Count tiles owned by 'player' that do NOT participate
  in any 3-in-a-row sequence.

LOGIC:
  matched_cells = set()
  for each (a,b,c) in LOSS_LINES:
      if board[a] == board[b] == board[c] == player:
          matched_cells.add(a, b, c)   # (shouldn't happen mid-game)

  unmatched = 0
  for each index i where board[i] == player:
      if i not in matched_cells:
          unmatched += 1
  return unmatched

NOTE:
  Since instant loss triggers before board fills, matched_cells
  should always be empty at terminal state. But keeping the
  logic robust handles edge cases.
```

### 3.7 `check_winner()` → Rewrite as `check_terminal(board, last_player)`

```
PURPOSE:
  Determine game outcome after a move.

PARAMETERS:
  board       — current board state
  last_player — who just moved ('X' or 'O')

RETURNS:
  'X_LOSS'   — X formed 3 in a row (X loses)
  'O_LOSS'   — O formed 3 in a row (O loses)
  'X_WIN'    — board full, X has more unmatched tiles
  'O_WIN'    — board full, O has more unmatched tiles
  'Draw'     — board full, equal unmatched tiles
  None       — game still ongoing

LOGIC:
  # Step 1: Check instant loss for last_player
  if has_instant_loss(board, last_player):
      return last_player + '_LOSS'    # e.g., 'X_LOSS'

  # Step 2: Check if board is full
  if no available moves:
      x_score = count_unmatched(board, 'X')
      o_score = count_unmatched(board, 'O')
      if x_score > o_score: return 'X_WIN'
      if o_score > x_score: return 'O_WIN'
      return 'Draw'

  # Step 3: Game continues
  return None

IMPORTANT NOTE:
  The signature now requires 'last_player' because instant-loss
  detection only applies to the player who just moved.
  (Opponent's existing 3-in-a-row would have been caught earlier.)
```

### 3.8 `is_terminal()` → Update Signature

```
CHANGE: Pass last_player through to check_terminal()

Before: is_terminal(board)
After:  is_terminal(board, last_player)

Returns True if check_terminal returns anything other than None.
```

### 3.9 `minimax()` — Significant Rewrite

```
SIGNATURE CHANGE:
  Add 'last_player' parameter to track who made the last move.

SCORE CONVENTION (new):
  AI = 'O' (maximizing)
  Human = 'X' (minimizing)

  Outcome → Score:
  ┌─────────────────────────────────┬───────────────────────────────┐
  │ Terminal Condition              │ Score                         │
  ├─────────────────────────────────┼───────────────────────────────┤
  │ O_LOSS (O formed 3 in a row)   │ -100 + depth (bad for AI)     │
  │ X_LOSS (X formed 3 in a row)   │ +100 - depth (good for AI)    │
  │ O_WIN  (O more unmatched)      │ +50 - depth                   │
  │ X_WIN  (X more unmatched)      │ -50 + depth                   │
  │ Draw                           │ 0                             │
  └─────────────────────────────────┴───────────────────────────────┘

  Depth adjustment:
    For losses: prefer SLOWER losses (opponent makes mistake)
    For wins:   prefer FASTER wins

ALPHA-BETA PRUNING:
  Retained — same structure, different score calculations.

RECURSIVE LOGIC CHANGE:
  After placing a move, pass the current player as 'last_player'
  to the recursive call so terminal detection knows who moved.

PSEUDO-STRUCTURE:
  minimax(board, depth, is_maximizing, last_player, alpha, beta):

      result = check_terminal(board, last_player)
      if result is not None:
          return score_map[result] adjusted by depth

      if is_maximizing:  # O's turn
          best = -inf
          for move in available_moves:
              board[move] = 'O'
              score = minimax(board, depth+1, False, 'O', alpha, beta)
              board[move] = ' '
              best = max(best, score)
              alpha = max(alpha, best)
              if beta <= alpha: break
          return best
      else:              # X's turn
          best = +inf
          for move in available_moves:
              board[move] = 'X'
              score = minimax(board, depth+1, True, 'X', alpha, beta)
              board[move] = ' '
              best = min(best, score)
              beta = min(beta, best)
              if beta <= alpha: break
          return best
```

### 3.10 `best_ai_move()` — Update Call Signature

```
CHANGE:
  After placing 'O' on the board for evaluation,
  pass 'O' as last_player to minimax.

  Also: starting minimax call passes 'O' as last_player
  (since AI just hypothetically placed 'O').

  score = minimax(board, 0, False, 'O', -inf, +inf)
  #                              ↑ last_player
  #                       ↑ next turn is Human (minimizing)
```

### 3.11 `get_human_move()` — Update Range

```
CHANGE: Valid input range 1-9 → 1-16

Before: available = [str(m+1) for m in get_available_moves(board)]
        prompt mentions "1-9"

After:  Same logic, but naturally handles 1-16.
        Update prompt text to say "1-16".
```

### 3.12 `play_game()` — Multiple Changes

```
CHANGE 1: Board display header
  Update cell layout display to show 4×4 grid (1-16).

CHANGE 2: check_winner() → check_terminal()
  Pass last_player to every terminal check call.

CHANGE 3: Interpret new result codes
  'X_LOSS' → "You formed 3 in a row — you lose!"
  'O_LOSS' → "AI formed 3 in a row — you win!"
  'X_WIN'  → "You win! Most unmatched tiles."
  'O_WIN'  → "AI wins! Most unmatched tiles."
  'Draw'   → "It's a draw!"

CHANGE 4: Show score at game end
  Display count_unmatched for both players so the result is clear.

CHANGE 5: Track last_player in game loop
  current_player is set before the move,
  after the move call check_terminal(board, current_player).
```

---

## Section 4 — Performance Considerations

### 4.1 Why 4×4 Minimax is Harder

```
3×3 TTT:  9! = 362,880 max nodes   → fast, no issue
4×4 game: 16! = 20,922,789,888,000 theoretical max

Even with alpha-beta pruning, pure minimax on 4×4 
with 16 empty cells is SLOW at game start.
```

### 4.2 Mitigation Strategy: Depth Limiting + Heuristic

```
Add a MAX_DEPTH constant (e.g., 6 or 8).

When depth >= MAX_DEPTH and no terminal state:
    return heuristic_score(board)

heuristic_score(board):
    # Estimate board value without full search
    ai_unmatched   = count_unmatched(board, 'O')
    human_unmatched = count_unmatched(board, 'X')

    # Penalty: how close is each player to forming 3 in a row?
    ai_danger    = count_near_loss_lines(board, 'O')  # lines with 2 O's
    human_danger = count_near_loss_lines(board, 'X')  # lines with 2 X's

    return (ai_unmatched - human_unmatched) 
           + (human_danger - ai_danger) * 0.5
    # AI wants human in danger (close to 3-in-a-row = closer to loss)
    # AI avoids its own danger
```

### 4.3 `count_near_loss_lines()` — New Helper

```
PURPOSE:
  Count how many LOSS_LINES have exactly 2 tiles of 'player'
  and 1 empty cell. These are "one move away from instant loss."

LOGIC:
  count = 0
  for (a,b,c) in LOSS_LINES:
      cells = [board[a], board[b], board[c]]
      if cells.count(player) == 2 and cells.count(' ') == 1:
          count += 1
  return count
```

---

## Section 5 — Complete Change Checklist

```
[ ] 1.  create_board()         → size 16 instead of 9
[ ] 2.  print_board()          → 4×4 layout, 2-char cell width
[ ] 3.  WIN_LINES              → rename to LOSS_LINES, replace content
[ ] 4.  has_instant_loss()     → NEW function
[ ] 5.  count_unmatched()      → NEW function
[ ] 6.  count_near_loss_lines()→ NEW function (heuristic helper)
[ ] 7.  check_winner()         → rewrite as check_terminal(board, last_player)
[ ] 8.  is_terminal()          → update signature with last_player
[ ] 9.  minimax()              → new scoring, new signature, depth limit
[ ] 10. best_ai_move()         → update minimax call signature
[ ] 11. get_human_move()       → update range to 1-16, prompt text
[ ] 12. play_game()            → new result codes, score display,
                                  track last_player in loop
[ ] 13. MAX_DEPTH constant     → add at module level (suggested: 6)
[ ] 14. heuristic_score()      → NEW function for depth-limited eval
[ ] 15. Update all docstrings  → reflect new game rules
[ ] 16. Update header comment  → new game name, rules summary
```

---

## Section 6 — Data Flow Diagram

```
play_game() loop
│
├─ Human moves
│   ├─ get_human_move(board) → index
│   ├─ board[index] = 'X'
│   └─ check_terminal(board, 'X')
│       ├─ has_instant_loss(board, 'X') ?
│       │   └─ YES → return 'X_LOSS' → display "You lose"
│       ├─ board full ?
│       │   └─ count_unmatched('X') vs count_unmatched('O')
│       │       └─ return 'X_WIN' / 'O_WIN' / 'Draw'
│       └─ None → continue
│
└─ AI moves
    ├─ best_ai_move(board)
    │   └─ for each move:
    │       ├─ board[move] = 'O'
    │       ├─ minimax(board, 0, False, 'O', -inf, +inf)
    │       │   ├─ check_terminal(board, last_player)
    │       │   │   ├─ has_instant_loss()
    │       │   │   └─ count_unmatched() if full
    │       │   ├─ depth >= MAX_DEPTH → heuristic_score()
    │       │   └─ recurse with alpha-beta pruning
    │       └─ board[move] = ' '
    ├─ board[best_move] = 'O'
    └─ check_terminal(board, 'O')
        └─ same logic as human branch
```

---

## Section 7 — Suggested Constants Block

```python
# ── Game Configuration ──────────────────────────────────────
BOARD_SIZE   = 16          # 4×4
MAX_DEPTH    = 6           # Depth limit for minimax on 4×4
INSTANT_LOSS_SCORE = 100   # Base score for instant-loss terminal
BOARD_FULL_SCORE   = 50    # Base score for unmatched-tile terminal

# ── All 3-consecutive sequences on 4×4 board ────────────────
LOSS_LINES = [
    # Rows
    (0,1,2),(1,2,3),(4,5,6),(5,6,7),
    (8,9,10),(9,10,11),(12,13,14),(13,14,15),
    # Columns
    (0,4,8),(4,8,12),(1,5,9),(5,9,13),
    (2,6,10),(6,10,14),(3,7,11),(7,11,15),
    # Diagonals ↘
    (0,5,10),(1,6,11),(4,9,14),(5,10,15),
    # Diagonals ↗
    (2,5,8),(3,6,9),(6,9,12),(7,10,13),
]
```