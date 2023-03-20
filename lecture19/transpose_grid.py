def transpose(grid: list) -> list:
    """
    Takes a list of lists and swaps rows for columns.
    """
    t_grid = []
    # assumes a constant number of columns
    n_rows = len(grid)
    n_cols = len(grid[0]) 

    # The key is looping over the columns first, then the rows
    for c in range(n_cols):
        t_row = []
        for r in range(n_rows):
            t_row.append(grid[r][c])
        t_grid.append(t_row)
    
    return t_grid

def pretty_print(grid: list) -> None:
    for row in grid:
        print(row)

def main() -> None:
    hard_coded = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    transposed = transpose(hard_coded)
    pretty_print(hard_coded)
    pretty_print(transposed)

main()