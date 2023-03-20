def transpose(grid: list) -> list:
    """
    Takes a list of lists and swaps rows for columns.
    """
    t_grid = []
    for i in range(len(grid)):
        t_col = []
        for j in range(len(grid[i])):
            t_col.append(grid[i][j])
        t_grid.append(t_col)
    
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