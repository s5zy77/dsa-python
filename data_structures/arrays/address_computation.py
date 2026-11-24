def address_1d(base, size, index, lower_bound=0):
    return base + size * (index - lower_bound)


def address_2d_row_major(base, size, i, j, rows, cols, row_lb=0, col_lb=0):
    return base + size * ((i - row_lb) * cols + (j - col_lb))


def address_2d_col_major(base, size, i, j, rows, cols, row_lb=0, col_lb=0):
    return base + size * ((j - col_lb) * rows + (i - row_lb))


if __name__ == "__main__":
    print("1D Address (Base=1000, Size=4, Index=5):", address_1d(1000, 4, 5))
    print("2D Row-Major [2][3] (4x5, Base=2000, Size=4):", address_2d_row_major(2000, 4, 2, 3, 4, 5))
    print("2D Col-Major [2][3] (4x5, Base=2000, Size=4):", address_2d_col_major(2000, 4, 2, 3, 4, 5))