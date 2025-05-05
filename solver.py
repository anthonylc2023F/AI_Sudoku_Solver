import sys

# For testing sake, this is an input for a 9x9 (hard) puzzle: 111111111122222222223333333333444444444455555555556666666666777777777788888888889

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

def convert_board(size, puzzle):
    if size == 9:
        return [[int(puzzle[i * 3 + j]) for j in range(3)] for i in range(3)]
    else:
        return [[int(puzzle[i * 9 + j]) for j in range(9)] for i in range(9)]
    # Convert to either vector<vector<int>> or an array of arrays of ints
    # Different based on if size == 9 or 81

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
def solve(size, puzzle):
    # Where the backtracking takes place
    return 0

# MRV heuristic - not required for our implementation but can be good to add
# def mrv():
    # Return the next block to solve

if __name__ == "__main__":
    # Check for input of a txt file first. If none, call user_input
    if len(sys.argv) == 3:
        print("Loading in files:", sys.argv[1], sys.argv[2])
        input = open(sys.argv[1], "r")
        with open(sys.argv[2], 'w') as output:
            for line in input:
                size = len(line.strip())
                output.write("Before:\n")
                print_board_to_file(size, line, output)
                puzzle_grid = convert_board(size, line)
            input.close()
            
    elif len(sys.argv) > 3 or len(sys.argv) == 2:
        print("Invalid usage. Either python solver.py with no arguments for manual mode or python solver.py input output for file mode.")
    else:
        print("No files passed in, running manual input mode.")
        puzzle, size = user_input() 
        print_board(size, puzzle)
        puzzle_grid = convert_board(size, puzzle)
    
    # puzzle is a list of digits that is size long

    # Will likely want to print the unsolved board and the solved board after backtracking is run
