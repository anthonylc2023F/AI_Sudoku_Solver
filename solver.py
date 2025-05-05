import sys

# For testing sake, this is an input for a 9x9 (hard) puzzle: 111111111122222222223333333333444444444455555555556666666666777777777788888888889


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


if __name__ == "__main__":
    # Check for input of a txt file first. If none, call user_input
    if len(sys.argv) == 2:
        print("Loading in file:", sys.argv[1])
    elif len(sys.argv) > 2:
        print("More than one file detected, only one file allowed at a time.")
    else:
        print("No files passed in, running manual input mode.")
    
    # puzzle is a list of digits that is size long
    puzzle, size = user_input() 
    print_board(size, puzzle)

    # Will likely want to print the unsolved board and the solved board after backtracking is run
