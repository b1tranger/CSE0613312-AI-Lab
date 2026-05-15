# Project Report: Avoid-3 Tic-Tac-Toe Variant

## Objective
The objective of this project is to develop an interactive and intellectually stimulating variant of the classic Tic-Tac-Toe game, termed "Avoid-3" (or Inverse Tic-Tac-Toe). The project aims to implement both a 2-player mode and an AI opponent mode to demonstrate applied artificial intelligence techniques in game development.

## Problem Statement
To create a real-world solution using the lab course concepts we learned, specifically focusing on **Adversarial Search** and the **Minimax Algorithm** with Alpha-Beta Pruning. The challenge is to adapt these classic AI algorithms, which are typically used for straightforward win-condition games, to an inverted, "avoidance" based game on a larger 4x4 grid, requiring the implementation of depth limits and custom heuristic evaluation functions.

## Solution
We developed a complete console-based game application (`inv_tictactoe.py`) that merges both Human vs. Human and Human vs. AI gameplay into a unified experience. The AI opponent leverages the Minimax algorithm to predict and counter the player's moves. Due to the expanded state space of a 4x4 board, a depth-limited search (depth=6) is utilized, supported by a heuristic evaluation function that assesses "danger zones" to prevent the AI from making suboptimal long-term moves.

## Game Logic
The game draws inspiration from classic 3x3 Tic-Tac-Toe but inverses the core mechanic and expands the board:
- **Board:** Played on a 4x4 grid (16 cells).
- **Instant Loss:** If a player forms *any* 3 consecutive tiles (in a row, column, or diagonal), they immediately lose the game.
- **Board-Full Win:** If the board fills up entirely without any player triggering an instant loss, the winner is decided by counting "unmatched tiles". The player with the most tiles that are *not* part of any 3-in-a-row configuration wins.
- **Draw:** If the board fills and both players have an equal number of unmatched tiles.

## Code Structure
The codebase (`inv_tictactoe.py`) is structured logically with modular functions and shared variables:

### Key Variables
- `BOARD_SIZE`: 16 (for the 4x4 grid).
- `MAX_DEPTH`: Limits the AI's Minimax search to 6 layers.
- `LOSS_LINES`: A comprehensive list of all possible 3-consecutive combinations on a 4x4 board.
- `INSTANT_LOSS_SCORE` & `BOARD_FULL_SCORE`: Constants used by Minimax to weight outcomes.

### Core Functions
- **Board Utilities:** `create_board()`, `print_board(board)`, `get_available_moves(board)`.
- **State Detection:** `has_instant_loss(board, player)`, `count_unmatched(board, player)`, `check_terminal(board, last_player)`.
- **AI Logic:** 
  - `count_near_loss_lines(board, player)`: Identifies threats (2 tiles + 1 empty space).
  - `heuristic_score(board)`: Evaluates non-terminal board states.
  - `minimax(board, depth, is_maximizing, last_player, alpha, beta)`: The core adversarial search algorithm.
  - `best_ai_move(board)`: Initiates the AI's decision-making process.
- **Game Flow:** `get_player_move(board, prompt)`, `decode_result(result, board, vs_ai)`, `play_game(vs_ai)`, and the `main()` menu.

## Real World Application
The concepts demonstrated in this project extend far beyond simple games. The underlying mechanics of Adversarial Search, Minimax, and Heuristic Evaluation are foundational to modern AI systems. Real-world applications include:
- **Strategic Decision Making:** Used in financial modeling to minimize potential maximum losses (Minimax principle).
- **Logistics and Routing:** Avoiding "danger zones" (traffic, hazards) is conceptually similar to avoiding 3-in-a-row loss lines.
- **Cybersecurity:** Adversarial search models can simulate attacks and defenses, predicting an opponent's moves to fortify vulnerabilities before they are exploited.

## Conclusion
This project successfully demonstrates the practical application of lab course concepts, specifically the Minimax algorithm and adversarial search techniques. By reversing the traditional rules of Tic-Tac-Toe and expanding the state space, the project highlights the flexibility of heuristic evaluations in solving complex, non-standard zero-sum games. The resulting application is both a fully functional interactive game and a robust proof-of-concept for applied artificial intelligence.
