import sys
import time

# For testing sake, this is an input for a 9x9 (hard) puzzle: 500467309903810427174203000231976854857124090496308172000089260782641005010000708

# TODO
"""
Methods to add:
    convert_board: Convert int with 81/9 digits to a readable board for parsing
        Likely using vectors
    valid_spot: Check if a block allows for a certain number
        Params may be number to input, readable board to change
    solve: Recursive function to add a possible digit to a block, and recursively solve the puzzle after that
        If return is false from next recursive call, try the next valid number for this square
        If true, return true if this number is valid (I think this is a given but might have to add a check)
        Base case: Puzzle is solved (no 0’s)
    (Maybe) Minimum value heuristic to check which blocks has the least number of options
        Return next block to check
"""

# Call if no file with puzzle specified
def user_input():
    print("Choose difficulty:")
    print("1. e for a 3x3 puzzle (easy)")
    print("2. h for a 9x9 puzzle (hard)")
    size = 0
    while size == 0:
        choice = input("Enter puzzle size: ")
        if choice == 'e':
            size = 3 * 3 # Total amount of numbers we will ask for to fill the puzzle
        elif choice == 'h':
            size = 9 * 9 # Total amount of numbers we will ask for to fill the puzzle
        else:
            print("Please choose either 'e' or 'h'")
    while True:
        puzzle = input(f"Enter {size} digits based on your puzzle (0 for empty): ")
        if len(puzzle) == size and puzzle.isdigit():
            return puzzle, size
        elif not puzzle.isdigit():
            print("Input must only be digits (0-9). Try again:")
        else:
            print(f"Wrong number of digits, you entered {len(puzzle)} digits, must be {size} digits. Try again:")


# Prints a board with size boxes
def print_board(size, puzzle):
    puzzle_string = str(puzzle) # Convert to string so we can split later
    if (size == 9): # 3x3
        print("-------------")
        for i in range(9, 0, -3): # Print input in rows of 3
            nums_to_print = puzzle_string[:3] # Slice off first 3 nums
            puzzle_string = puzzle_string[3:] # Remove first 3 nums from original puzzle
            string = "|"
            for num in nums_to_print:
                string += f" {num} |"
            print(string)
            print("-------------")
    else: # 9x9 - a lot longer than that ^ print bc I wanted to distinguish between each of the 3x3's within the 9x9
        print(" ------------- ------------ ------------")
        y = 1 # Used in separating 3x3's
        for i in range(81, 0, -9): # Print input in rows of 9
            nums_to_print = puzzle_string[:9] # Slice off first 9 nums
            puzzle_string = puzzle_string[9:] # Remove first 9 nums from original puzzle
            string = "||"
            x = 1 # Used in separating 3x3's
            for num in nums_to_print:
                string += f" {num} |"
                if x % 3 == 0: # Used in separating 3x3's
                    string += "|"
                x += 1
            print(string)
            print(" ------------- ------------ ------------")
            if y % 3 == 0 and i != 9: # Used in separating 3x3's
                print(" ------------- ------------ ------------")
            y += 1

# Prints a board with size boxes to an output file
def print_board_to_file(size, puzzle, out):
        puzzle_string = str(puzzle) # Convert to string so we can split later
        if (size == 9): # 3x3
            out.write("-------------\n")
            for i in range(9, 0, -3): # Print input in rows of 3
                nums_to_print = puzzle_string[:3] # Slice off first 3 nums
                puzzle_string = puzzle_string[3:] # Remove first 3 nums from original puzzle
                string = "|"
                for num in nums_to_print:
                    string += f" {num} |"
                out.write(string + "\n")
                out.write("-------------\n")
            out.write("==========================================\n")

        else: # 9x9 - a lot longer than that ^ print bc I wanted to distinguish between each of the 3x3's within the 9x9
            out.write(" ------------- ------------ ------------\n")
            y = 1 # Used in separating 3x3's
            for i in range(81, 0, -9): # Print input in rows of 9
                nums_to_print = puzzle_string[:9] # Slice off first 9 nums
                puzzle_string = puzzle_string[9:] # Remove first 9 nums from original puzzle
                string = "||"
                x = 1 # Used in separating 3x3's
                for num in nums_to_print:
                    string += f" {num} |"
                    if x % 3 == 0: # Used in separating 3x3's
                        string += "|"
                    x += 1
                out.write(string + "\n")
                out.write(" ------------- ------------ ------------\n")
                if y % 3 == 0 and i != 9: # Used in separating 3x3's
                    out.write(" ------------- ------------ ------------\n")
                y += 1
            out.write("==========================================\n")

def convert_board_to_grid(size, puzzle):
    if size == 9:
        return [[int(puzzle[i * 3 + j]) for j in range(3)] for i in range(3)]
    else:
        return [[int(puzzle[i * 9 + j]) for j in range(9)] for i in range(9)]
    # Convert to either vector<vector<int>> or an array of arrays of ints
    # Different based on if size == 9 or 81

def convert_grid_to_board(puzzle):
    return ''.join(str(cell) for row in puzzle for cell in row)
        

# row and column will be None if size == 9
def valid_spot(size, puzzle, row, column, number):

    if (size == 9):
        # Check mini 3x3
        for x in range(3):
            for y in range(3):
                if puzzle[x][y] == number:
                    return False
        return True
    else:

        # Check column (y axis)
        for y in range(9):
            if puzzle[y][column] == number:
                return False

        # Check row (x axis)
        for x in range(9):
            if puzzle[row][x] == number:
                return False
            
        # Check current 3x3
        # check what "block" we are working with
        blockRow = row - (row % 3)
        blockColumn = column - (column % 3)

        for x in range(3):
            for y in range(3):
                if puzzle[x + blockRow][y + blockColumn] == number:
                    return False
                
        return True

    # If a 3x3, just check if the current number exists in the puzzle
    # If a 9x9, must check current 3x3, the column, and row if the number we are trying exists in any of the 3
    # Return true if valid spot for this number, false if not

# Recursive backtracking algorithm
def solve_hard(puzzle, row, col):
    # If we reached the last spot successfully, return True
    if row == 8 and col == 9:
        return True
   
    # If we reached the end of a row, move to the next
    elif col == 9:
        row += 1
        col = 0


    # If this spot is already filled move to the next
    if puzzle[row][col] != 0:
        return solve_hard(puzzle, row, col + 1)
   
    # Try putting numbers from 1-9 here until we find one that works with the puzzle
    for i in range(1, 10):
        if valid_spot(81, puzzle, row, col, i):
            puzzle[row][col] = i
            if solve_hard(puzzle, row, col + 1):
                return True
            puzzle[row][col] = 0
    return False


def solve(puzzle):
    #solve_hard(puzzle, 0, 0)
    mrv(puzzle)


# MRV heuristic helper method
def find_best_cell(puzzle):
    minimum_options = 10 # Max options is 9, so make it 1 higher
    best_cell = None # no best cell to start off with

    # loop through rows/columns
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                options = 0 # start with 0 options
                
                for number in range(1, 10): # run through all the numbers
                    if valid_spot(81, puzzle, row, column, number):
                        options += 1 # another valid option
                if options < minimum_options: # less options than minimum options
                    minimum_options = options
                    best_cell = (row, column)
                    if minimum_options == 1: # Cant do better than this
                        return best_cell
    return best_cell




# MRV heuristic - not required for our implementation but can be good to add
def mrv(puzzle):
    best_cell = find_best_cell(puzzle)
    if not best_cell: # if no cell found, return True as puzzle must be solved
        return True
    
    row = best_cell[0]
    column = best_cell[1]

    for number in range(1, 10): # Loop through every number
        if valid_spot(81, puzzle, row, column, number): # check if valid spot
            puzzle[row][column] = number
            if mrv(puzzle):
                return True
            puzzle[row][column] = 0 # Backtracking
    return False


if __name__ == "__main__":
    # Check for input of a txt file first. If none, call user_input
    if len(sys.argv) == 3:
        print("Loading in files:", sys.argv[1], sys.argv[2])
        input = open(sys.argv[1], "r")
        startTime = time.time()
        with open(sys.argv[2], 'w') as output:
            for line in input:
                line = line.strip()
                size = len(line.strip())
                output.write("Before:\n")
                print_board_to_file(size, line, output)
                puzzle_grid = convert_board_to_grid(size, line)
                solve(puzzle_grid)
                puzzle_grid = convert_grid_to_board(puzzle_grid)
                output.write(f"After:\n")
                print_board_to_file(size, puzzle_grid, output)
                output.write("==========================================\n")
            endTime = time.time()
            output.write(f"After: (Elapsed time: {endTime - startTime})\n")
            input.close()
            
    elif len(sys.argv) > 3 or len(sys.argv) == 2:
        print("Invalid usage. You have two options:")
        print("python solver.py - for manual input of sudoku puzzle")
        print("python solver.py <input file> <output file> - to use an input file")
    else:
        print("No files passed in, running manual input mode.")
        puzzle, size = user_input() 
        print_board(size, puzzle)
        puzzle_grid = convert_board_to_grid(size, puzzle)
        solve(puzzle_grid)
        puzzle = convert_grid_to_board(puzzle_grid)
        print_board(size, puzzle)
    
    # puzzle is a list of digits that is size long

    # Will likely want to print the unsolved board and the solved board after backtracking is run
