def numberAmazonGoStores(rows, column, grid):
    # WRITE YOUR CODE HERE
    stores_proto = [[0 for col in range(column)] for r in range(rows)]
    stores_open = 0
    for row in range(rows):
        for col in range(column):
            stores_open += isStoreValidPoint(grid, stores_proto, row, col, rows, column)
    return stores_open


def isStoreValidPoint(grid, stores_proto, row, col, total_rows, total_cols):
    if not is_valid_(total_rows, total_cols, row, col) or stores_proto[row][col] == 1 or grid[row][col] == 0:
        return 0
    stores_proto[row][col] = 1
    isStoreValidPoint(grid, stores_proto, row, col + 1, total_rows, total_cols)
    isStoreValidPoint(grid, stores_proto, row, col - 1, total_rows, total_cols)
    isStoreValidPoint(grid, stores_proto, row + 1, col, total_rows, total_cols)
    isStoreValidPoint(grid, stores_proto, row - 1, col, total_rows, total_cols)
    return 1


def is_valid_(rows, cols, row, col):
    return 0 <= row < rows and 0 <= col < cols

x = [[1,1,0, 0],
     [0,0,0,0],
     [0,0,1,1],
     [0,0,0,0]]
visits = 0
print(numberAmazonGoStores(4, 4, x))
