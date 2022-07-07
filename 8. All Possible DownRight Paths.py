def count_all_paths(rows, cols, c_row=0, c_col=0):
    if c_row >= rows or c_col >= cols:
        return 0
    if c_row == rows - 1 and c_col == cols - 1:
        return 1

    n_unique_paths = 0

    n_unique_paths += count_all_paths(rows, cols, c_row, c_col + 1)  # Right
    n_unique_paths += count_all_paths(rows, cols, c_row + 1, c_col)  # Down
    return n_unique_paths


rows = int(input())
cols = int(input())

print(count_all_paths(rows, cols))
