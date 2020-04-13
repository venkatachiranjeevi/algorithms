from collections import deque


def minHour(rows, columns, grid):
    times = 0
    Q = deque([])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                Q.append((i, j))

    while (Q):
        for _ in range(len(Q)):
            x, y = Q.popleft()
            for dir in directions:
                i = x + dir[0]
                j = y + dir[1]
                if 0 <= i < rows and 0 <= j < columns and grid[i][j] == 0:
                    grid[i][j] = 1
                    Q.append((i, j))
        times += 1
    return max(0, times - 1)

x = minHour(4, 5, [[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]])

print(x)