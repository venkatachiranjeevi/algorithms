def lengthEachScene(inputList):
    # WRITE YOUR CODE HERE
    index_counter = {}
    for index in range(len(inputList)):
        index_counter[inputList[index]] = index
    result = []
    left_p = 0
    right_p = 0
    for index in range(len(inputList)):
        right_p = max(right_p, index_counter[inputList[index]])
        if right_p == index:
            result.append(1+right_p - left_p)
            left_p = right_p + 1

    return result
#
# x = lengthEachScene(['a', 'b', 'c', 'd', 'a', 'e', 'f', 'g', 'h', 'i', 'j', 'e'])
# print(x)

def numberAmazonGoStores(rows, column, grid):
    # WRITE YOUR CODE HERE
    stores_proto = [[0 for col in range(column)] for r in range(rows)]


def isStoreVisited(grid, stores_proto, row, col, total_rows, total_cols):
    if not is_valid_(total_rows, total_cols, row, col) or stores_proto[row][col] == 1 or grid[row][col] == 0:
        return 0

    return 1


def is_valid_(rows, cols, row, col):
    return 0 <= row < rows and 0 <= col < cols




def get_number_of_islands(binaryMatrix):
    rows = len(binaryMatrix)
    cols = len(binaryMatrix[0])
    # you can use Set if you like
    # or change the content of binaryMatrix as it is visited
    visited = [[0 for col in range(cols)] for r in range(rows)]
    number_of_island = 0
    for row in range(rows):
        for col in range(cols):
            number_of_island += get_island(binaryMatrix, row, col, visited)
    return number_of_island


# get a continuous island
def get_island(binaryMatrix, row, col, visited):
    if not is_valid(binaryMatrix, row, col) or visited[row][col] == 1 or binaryMatrix[row][col] == 0:
        return 0

    # mark as visited
    visited[row][col] = 1
    get_island(binaryMatrix, row, col + 1, visited)
    get_island(binaryMatrix, row, col - 1, visited)
    get_island(binaryMatrix, row + 1, col, visited)
    get_island(binaryMatrix, row - 1, col, visited)
    return 1


def is_valid(binaryMatrix, row, col):
    rows = len(binaryMatrix)
    cols = len(binaryMatrix[0])
    return row >= 0 and row < rows and col >= 0 and col < cols

binaryMatrix = [ [1,    1,    0,    0],
                 [0,    0,    1,   0],
                 [0, 0, 0, 0],
                 [1, 0,    1,    1],
                 [1, 1, 1, 1] ]

x = [[1,1,0, 0],
     [0,0,0,0],
     [0,0,1,1],
     [0,0,0,0]]
print(get_number_of_islands(x))