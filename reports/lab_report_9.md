# Lab Report 9

## Title
Adversarial Search and the Minimax Algorithm

## Theory
Adversarial search is an AI technique used for decision-making in competitive, multi-agent environments, particularly zero-sum games where one player's gain is the opponent's loss (e.g., Tic-Tac-Toe, Chess). 
The **Minimax Algorithm** is a recursive strategy where the AI assumes both players play optimally. The algorithm navigates a Game Tree, simulating all possible moves. The "Maximizer" tries to maximize the score (win), while the "Minimizer" tries to select moves that result in the lowest possible score for the Maximizer (lose).

## Algorithms
Minimax Algorithm with a Heuristic Evaluation Function for Tic-Tac-Toe.

## Code Implementation
```python
player, opponent = 'x', 'o' 

def evaluate(b): 
    # Checks Rows, Cols, and Diagonals
    for row in range(3):     
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):        
            if (b[row][0] == player): return 10
            elif (b[row][0] == opponent): return -10
    # ... Similar checks for columns and diagonals ...
    return 0

def minimax(board, depth, isMax): 
    score = evaluate(board)
    if (score == 10) or (score == -10): return score
    if not isMovesLeft(board): return 0

    if (isMax):     
        best = -1000 
        for i in range(3):         
            for j in range(3):
                if (board[i][j]=='_'):
                    board[i][j] = player 
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best
    else:
        best = 1000 
        for i in range(3):         
            for j in range(3):
                if (board[i][j] == '_'):
                    board[i][j] = opponent 
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best

def findBestMove(board): 
    # Starts the minimax process for every empty cell to find the best move
    # ...
```

## Output
```
The value of the best Move is : 10

The Optimal Move is :
ROW: 2  COL: 0
```

## Discussion
The evaluation function correctly identifies terminal states (wins/losses). The recursive `minimax` function effectively explores the entire state space of the Tic-Tac-Toe game because the state space is relatively small. However, for more complex games like Chess or Go, traversing the entire game tree is computationally impossible. In those cases, optimizations like Alpha-Beta Pruning (which skips branches that can't possibly affect the final decision) or depth limits are required.

## Conclusion
We successfully implemented the Minimax algorithm to find the optimal move in a zero-sum game. This demonstrated how AI can model adversarial situations and make perfect decisions by simulating future game states.
