# AI_Sudoku_Solver
- To test out for yourself, run "python solver.py test.txt output.txt"
- This will run the solver on the puzzle inside test.txt and output the results to output.txt
- You can also create your own txt files similarly to test.txt, or simply run 
the solver without arguments ("python solver.py") in which it will prompt for input then

# General Strategy:
Solving:
- Backtracking algorithm
- Minimum remaining value (MRV) heuristic to pick next space to solve

Input:
- The number input will be from left to right, top to bottom 
  - Order the numbers would be input for a 3x3:
 -----------------
|  1  |  2  |  3  |
 -----------------
|  4  |  5  |  6  |
 -----------------
|  7  |  8  |  9  |
 -----------------

Display
- Prints the before (input) and after (solved puzzle)
- Different display methods based on 3x3 or 9x9
