# AI_Sudoku_Solver

# General Strategy:
Solving:
- Backtracking
- “Algorithm to Solve Sudoku”
  - https://www.geeksforgeeks.org/sudoku-backtracking-7/
- Should probably use forward checking potentially instead of or alongside backtracking
- Minimum remaining value (MRV) heuristic would be great to incorporate to probably increase speed (and uniqueness from others)

Input:
- Want to allow for user input (so it’s different from others)
  - Maybe a little pop-up
- Probably gonna have an input in the form of the following:
  - First character is e or h for easy or hard
    - Easy is 1 block (3x3), hard is 9 (9x9)
  - The number input will be from left to right, top to bottom 
    - Order the numbers would be input for a 3x3:
 -----------------
|  1  |  2  |  3  |
 -----------------
|  4  |  5  |  6  |
 -----------------
|  7  |  8  |  9  |
 -----------------
  - Maybe have a user input somehow
    - If no txt file is specified when running, ask for user input(?)

Display
- Will likely print formatted to look like a sudoku board to a human
- Print the before (input) and after (solved puzzle)
- Different display methods based on 3x3 or 9x9
- Maybe have a special pop-up display to show which of the numbers in the solved puzzle were originally given (just a thought to be unique)
