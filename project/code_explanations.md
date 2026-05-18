# Tic-Tac-Toe Code Explanations

This document provides a detailed breakdown of the code flow, key variables, and functions for each of the three Tic-Tac-Toe game variants in the project.

---

## 1. `tictactoe_vs_player.py`

This script implements a classic 2-player (Human vs. Human) Tic-Tac-Toe game on a 3x3 board.

### **Code Flow**
1. The game starts by executing the `main()` function, which displays a welcome message and prompts the players for their names.
2. The game enters a `while True` loop, managing the overall session and keeping track of scores.
3. For each round, `play_round()` is called. It creates an empty board and enters a turn loop.
4. Inside the turn loop, the board is displayed, and the current player is prompted to make a move via `get_player_move()`.
5. The move is applied to the board, and `check_winner()` checks if the game has ended (win or draw).
6. If the game ends, the result is returned, scores are updated, and the user is prompted to play again.

### **Key Variables**
- **`WIN_LINES`**: A list of tuples, where each tuple represents a winning combination of indices (rows, columns, diagonals).
- **`board`**: A list of 9 strings representing the 3x3 grid. Empty cells are denoted by `" "`.
- **`scores`**: A dictionary tracking the number of wins for `"X"`, `"O"`, and `"Draw"`.
- **`players`**: A dictionary mapping the player symbol (`"X"` or `"O"`) to their respective name and symbol.
- **`turn_order`**: A list `["X", "O"]` used to cycle turns using `turn_index % 2`.

### **Functions**
- **`create_board()`**: Initializes and returns a list of 9 empty strings representing the board.
- **`print_board(board)`**: Formats and prints the board. Empty cells display their 1-based index to help players choose their move.
- **`get_available_moves(board)`**: Scans the board and returns a list of indices that are currently empty.
- **`check_winner(board)`**: Iterates through `WIN_LINES` to see if any player has 3 symbols in a row. Returns `"X"`, `"O"`, `"Draw"`, or `None` if the game is ongoing.
- **`get_player_move(board, player_name, symbol)`**: Prompts the user for input, ensuring they pick a valid, empty cell index.
- **`print_scores(scores, names)`**: Displays the current scoreboard for both players and draws.
- **`play_round(names)`**: Manages a single round of the game, alternating turns between the two players until there's a winner or draw.
- **`main()`**: The entry point. Handles session-level data like player names, score accumulation, and the play-again prompt.

---

## 2. `tictactoe_vs_AI.py`

This script implements a Human vs. AI Tic-Tac-Toe game on a 3x3 board, where the AI uses the Minimax algorithm with Alpha-Beta Pruning to play optimally.

### **Code Flow**
1. The game is initialized in `play_game()`, defining the Human as `"X"` (going first) and the AI as `"O"`.
2. A turn-based loop begins.
3. On the Human's turn, `get_human_move()` prompts for a valid cell index.
4. On the AI's turn, `best_ai_move()` is called. This triggers the recursive `minimax()` algorithm to evaluate all possible future board states and pick the optimal move.
5. After each move, `check_winner()` is called. If a terminal state is reached, the result is printed, and the loop ends.
6. The main block prompts to restart the game if desired.

### **Key Variables**
- **`WIN_LINES`**: Same as the 2-player version, representing all possible 3-in-a-row combinations.
- **`alpha`** / **`beta`**: Variables used in the Minimax algorithm to prune branches of the game tree that don't need to be explored.
- **`current_player`**: Keeps track of whose turn it is (`"X"` or `"O"`).

### **Functions**
- **`minimax(board, depth, is_maximizing, alpha, beta)`**: The core AI logic. It recursively simulates all possible moves. The AI (`is_maximizing`) tries to maximize the score, while the Human (`not is_maximizing`) is assumed to play optimally to minimize the score. It includes Alpha-Beta pruning to speed up computation. Returns a heuristic score: positive for AI win, negative for Human win.
- **`best_ai_move(board)`**: The wrapper for `minimax()`. It iterates through all available immediate moves, uses `minimax()` to score each one, and returns the move with the highest score.
- **`get_human_move(board)`**: Validates and returns the user's chosen cell index.
- **`is_terminal(board)`**: A helper function to check if the game has ended.
- ***(Includes standard board utilities like `create_board()`, `print_board()`, `check_winner()`, and `get_available_moves()` identical/similar to the 2-player script).*

---

## 3. `inv_tictactoe_vs_AI.py`

This script implements an "Avoid-3" variant on a larger 4x4 board. Forming 3-in-a-row loses the game, and if the board fills, the player with the most unmatched tiles wins. The AI uses a depth-limited Minimax with a heuristic evaluation function.

### **Code Flow**
1. `play_game()` initializes the game. The human (`"X"`) plays against the AI (`"O"`).
2. The turn loop begins. The Human enters a move, or the AI calculates its move using `best_ai_move()`.
3. Due to the 4x4 board complexity, `minimax()` is restricted by `MAX_DEPTH`. If the search reaches this depth without finding a terminal state, it relies on `heuristic_score()`.
4. After every move, `check_terminal()` evaluates if the move caused an instant loss (3-in-a-row) or if the board is full.
5. If terminal, `decode_result()` translates the outcome into a user-friendly message and the game ends.

### **Key Variables**
- **`BOARD_SIZE`**: Set to 16 for the 4x4 grid.
- **`MAX_DEPTH`**: Set to 6. Prevents the Minimax algorithm from taking too long by limiting how many turns ahead it looks.
- **`LOSS_LINES`**: Contains all possible 3-consecutive lines on a 4x4 board (rows, columns, and diagonals). There are sliding windows because 4 cells in a row contain two distinct 3-cell lines.
- **`INSTANT_LOSS_SCORE`** / **`BOARD_FULL_SCORE`**: Constants used in Minimax to heavily weight instant losses/wins over tie-breakers.

### **Functions**
- **`has_instant_loss(board, player)`**: Scans `LOSS_LINES` to check if a player just formed a 3-in-a-row, returning `True` if they did (meaning they lose).
- **`count_unmatched(board, player)`**: When the board is full, this counts how many tiles a player has that are NOT part of any 3-consecutive line.
- **`check_terminal(board, last_player)`**: Determines if the game has ended, either through an instant loss by the `last_player` or because the board is full (returning the winner based on unmatched tile counts).
- **`count_near_loss_lines(board, player)`**: Scans the board for lines that have 2 of the player's tiles and 1 empty space. These are high-danger zones.
- **`heuristic_score(board)`**: Used when Minimax reaches `MAX_DEPTH`. It calculates a score based on the difference in unmatched tiles and the difference in "danger zones" between the AI and Human.
- **`minimax(board, depth, is_maximizing, last_player, alpha, beta)`**: A depth-limited version of Minimax. It rewards slower losses and faster wins by incorporating `depth` into the terminal scores. If `MAX_DEPTH` is hit, it falls back to `heuristic_score()`.
- **`best_ai_move(board)`**: Iterates over valid moves, scoring them via `minimax()`, and returns the best move for the AI.
- **`decode_result(result, board)`**: Translates terminal state string codes (like `"X_LOSS"`) into readable text and score summaries.
- **`play_game()`**: Manages the main game loop, displaying the board and toggling turns.

---

## 4. `inv_tictactoe_vs_player.py`

This script implements an "Avoid-3" variant on a larger 4x4 board for two human players. It is the multiplayer version of the Avoid-3 game.

### **Code Flow**
1. `play_game()` initializes the game. Player 1 (`"X"`) plays against Player 2 (`"O"`).
2. The turn loop begins. Each player is prompted to enter a move via `get_player_move()`.
3. After every move, `check_terminal()` evaluates if the move caused an instant loss (3-in-a-row) or if the board is full.
4. If terminal, `decode_result()` translates the outcome into a user-friendly message and the game ends.

### **Key Variables**
- **`BOARD_SIZE`**: Set to 16 for the 4x4 grid.
- **`LOSS_LINES`**: Contains all possible 3-consecutive lines on a 4x4 board (rows, columns, and diagonals).

### **Functions**
- **`has_instant_loss(board, player)`**: Scans `LOSS_LINES` to check if a player just formed a 3-in-a-row, returning `True` if they did (meaning they lose).
- **`count_unmatched(board, player)`**: When the board is full, this counts how many tiles a player has that are NOT part of any 3-consecutive line.
- **`check_terminal(board, last_player)`**: Determines if the game has ended, either through an instant loss by the `last_player` or because the board is full.
- **`get_player_move(board, player)`**: Prompts the current player to input a valid cell index.
- **`decode_result(result, board)`**: Translates terminal state string codes (like `"X_LOSS"`) into readable text and score summaries for a 2-player match.
- **`play_game()`**: Manages the main game loop, displaying the board and toggling turns between Player 1 and Player 2.


---

## 5. `inv_tictactoe.py`

This script implements an "Avoid-3" variant on a 4x4 board, featuring both Human vs. AI and 2-Player (Human vs. Human) modes. Forming 3-in-a-row loses the game immediately. If the board fills up without any instant losses, the player with the most unmatched tiles (tiles not part of any 3-consecutive line) wins. The AI uses a depth-limited Minimax algorithm with a custom heuristic evaluation.

### **Code Flow**
1. `main()` presents an interactive menu allowing the user to select either "Play vs AI", "Play vs Human (2 Player)", or "Quit".
2. Based on the choice, `play_game(vs_ai)` initializes the game. It displays the rules and the board.
3. The turn loop begins. For a human turn, `get_player_move()` prompts for a valid cell index. For an AI turn, `best_ai_move()` determines the optimal move using Minimax.
4. Due to the 4x4 board complexity, `minimax()` is restricted by `MAX_DEPTH`. If the search reaches this depth without finding a terminal state, it relies on `heuristic_score()`.
5. After every move, `check_terminal()` evaluates if the move caused an instant loss (3-in-a-row) or if the board is full.
6. If the game is terminal, `decode_result()` translates the outcome into a user-friendly message, displays the final unmatched tiles count, and the game loop breaks, returning to the main menu.

### **Key Variables**
- **`BOARD_SIZE`**: Set to 16 for the 4x4 grid.
- **`MAX_DEPTH`**: Set to 6. Prevents the Minimax algorithm from taking too long by limiting how many turns ahead it explores.
- **`LOSS_LINES`**: Contains all possible 3-consecutive lines on a 4x4 board (rows, columns, and diagonals). Note that there are sliding windows because a single 4-cell line contains two overlapping 3-cell sequences.
- **`INSTANT_LOSS_SCORE`** / **`BOARD_FULL_SCORE`**: Constants used in Minimax to heavily weight instant outcomes over heuristic tie-breakers.

### **Functions**
- **`has_instant_loss(board, player)`**: Scans `LOSS_LINES` to check if a player just formed a 3-in-a-row, returning `True` if they did (meaning they lose).
- **`count_unmatched(board, player)`**: When the board is full, this counts how many tiles a player has that are NOT part of any 3-consecutive line.
- **`check_terminal(board, last_player)`**: Determines if the game has ended, returning string flags (e.g., `"X_LOSS"`, `"O_WIN"`, `"Draw"`) based on instant loss or full-board conditions.
- **`count_near_loss_lines(board, player)`**: Scans the board for lines that have 2 of the player's tiles and 1 empty space. These represent high-danger zones.
- **`heuristic_score(board)`**: Used when Minimax reaches `MAX_DEPTH`. It calculates a score based on the difference in unmatched tiles and the difference in "danger zones" between the AI and Human.
- **`minimax(board, depth, is_maximizing, last_player, alpha, beta)`**: A depth-limited version of Minimax using Alpha-Beta pruning. It evaluates terminal states (accounting for depth to prioritize faster wins/slower losses) and falls back to `heuristic_score()` at the depth limit.
- **`best_ai_move(board)`**: Iterates over valid moves, scoring them via `minimax()`, and returns the best move for the AI.
- **`decode_result(result, board, vs_ai)`**: Translates terminal state string codes into readable text and score summaries, dynamically adjusting the text depending on whether the game was against the AI or another player.
- **`play_game(vs_ai)`**: Manages the main game loop, displaying the board, and toggling turns.
- **`main()`**: Displays the main menu and handles game mode selection and replay logic.

