def find_empty_spot(puzzle):
    #finds the next emtpy cell (represented w -1) and returns the row and col it is at
    #returns None, None if the puzzle is completely filled (no empty cell)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
            
    return None, None #no empty cell found

def is_valid(puzzle, guess, row, col):
    
    #checking if the guess repeats in the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #checking if the guess repeats in a col
    col_vals = [puzzle[r][col] for r in range(9)]
    if guess in col_vals:
        return False
    
    #checking if the guess repeats in a square
    row_start = (row//3) * 3
    col_start = (col//3) * 3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    return True
    
def sudoko_solver(puzzle):

    row, col = find_empty_spot(puzzle)

    if row is None:
        return True #if there is no empty spot then the puzzle is solved and we're done.
    
    #otherwise, make a guess from 1 to 9 and place it in that empty spot
    for guess in range(1,10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if(sudoko_solver(puzzle)):
                return True
            
        puzzle[row][col] = -1

    return False #none of the combinations work, the puzzle is unsolvable    

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(sudoko_solver(example_board))
    print(example_board)       