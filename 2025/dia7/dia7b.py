#!/usr/bin/env python3
# day7_part2_timelines.py
# Lee input.txt (mapa con S, ^ y .) y calcula el número total de timelines
# según la interpretación many-worlds (Part Two).

from functools import lru_cache
import sys

# MOVIMIENTO: buscar el siguiente '^' en la misma columna, empezando en row (inclusive)
# si no hay '^' hasta el final => se sale (1 timeline).
# cuando se encuentra '^' en (r,c) -> dos nuevos inicios: (r+1, c-1) y (r+1, c+1).
# si cualquiera de esos inicios está fuera (col fuera de rango o fila >= n) -> cuenta como 1.

def read_grid(path="input.txt"):
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    # quitar líneas vacías al final accidentalmente
    while lines and lines[-1] == "":
        lines.pop()
    grid = [list(line) for line in lines]
    return grid

def find_S(grid):
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch == 'S':
                return i, j
    return None

def timelines_count(grid):
    if not grid:
        return 0
    n = len(grid)
    m = max(len(r) for r in grid)
    # normalizar filas a longitud m rellenando con '.' para evitar IndexError
    for r in grid:
        if len(r) < m:
            r.extend(['.'] * (m - len(r)))

    @lru_cache(maxsize=None)
    def count_from(pos):
        # pos is (r, c) starting position of a single particle (it will start moving downward from here)
        r, c = pos
        # if starting column out of bounds -> it's already outside -> counts as 1 timeline (exited)
        if c < 0 or c >= m:
            return 1
        # if starting row is beyond bottom -> exited
        if r >= n:
            return 1

        # Move down from (r,c) to find first splitter '^' in same column at row >= r
        rr = r
        while rr < n and grid[rr][c] != '^':
            rr += 1

        if rr >= n:
            # no splitter below; particle exits => 1 timeline
            return 1

        # found splitter at (rr, c). It stops there and spawns two starting positions:
        left_start = (rr + 1, c - 1)
        right_start = (rr + 1, c + 1)

        # The total timelines from this particle equals sum of timelines from each spawned particle.
        left_count = count_from(left_start)
        right_count = count_from(right_start)
        return left_count + right_count

    # find S and start from the cell immediately below S
    S = find_S(grid)
    if S is None:
        raise ValueError("No 'S' found in input.txt")
    start = (S[0] + 1, S[1])
    return count_from(start)

if __name__ == "__main__":
    grid = read_grid("input.txt")
    try:
        result = timelines_count(grid)
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(2)
    print(result)
