from collections import deque

DIRS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def read_grid(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f if line.rstrip("\n")]
    grid = [list(line) for line in lines]
    if not grid:
        return grid
    m = max(len(row) for row in grid)
    for row in grid:
        if len(row) < m:
            row.extend(['.'] * (m - len(row)))
    return grid

def total_removibles(grid):
    n = len(grid)
    m = len(grid[0]) if n else 0

    neigh = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '@': continue
            cnt = 0
            for di,dj in DIRS:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '@':
                    cnt += 1
            neigh[i][j] = cnt

    q = deque()
    inq = [[False]*m for _ in range(n)]
    removed = [[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@' and neigh[i][j] < 4:
                q.append((i,j))
                inq[i][j] = True

    total = 0
    while q:
        i,j = q.popleft()
        if removed[i][j]:
            continue
        if grid[i][j] != '@':
            removed[i][j] = True
            continue
        grid[i][j] = '.'
        removed[i][j] = True
        total += 1
        for di,dj in DIRS:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '@':
                neigh[ni][nj] -= 1
                if neigh[ni][nj] < 4 and (not inq[ni][nj]) and (not removed[ni][nj]):
                    q.append((ni,nj))
                    inq[ni][nj] = True

    return total

if __name__ == "__main__":
    grid = read_grid("input.txt")
    result = total_removibles(grid)
    print(result)
