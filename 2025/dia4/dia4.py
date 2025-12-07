from typing import List, Tuple

def leer_mapa(path: str) -> List[List[str]]:
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f if line.rstrip("\n")]
    # Representamos como matriz de caracteres
    grid = [list(line) for line in lines]
    return grid

def vecinos_8(i: int, j: int, n: int, m: int) -> List[Tuple[int,int]]:
    dirs = [(-1,-1), (-1,0), (-1,1),
            (0,-1),         (0,1),
            (1,-1),  (1,0), (1,1)]
    res = []
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            res.append((ni, nj))
    return res

def contar_accesibles(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
    if not grid:
        return 0, grid
    n = len(grid)
    m = max(len(row) for row in grid)
    # Asegurar rectangularidad rellenando con '.' donde faltan columnas
    for row in grid:
        if len(row) < m:
            row.extend('.' * (m - len(row)))

    marcado = [row.copy() for row in grid]  # copia para marcar con 'x'
    total = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] != '@':
                continue
            count_adj = 0
            for ni, nj in vecinos_8(i, j, n, m):
                if grid[ni][nj] == '@':
                    count_adj += 1
            if count_adj < 4:
                marcado[i][j] = 'x'
                total += 1
            else:
                # opcional: dejar '@' o marcar con otro símbolo
                marcado[i][j] = grid[i][j]
    return total, marcado

def imprimir_mapa(grid: List[List[str]]):
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    mapa = leer_mapa("input.txt")
    total, mapa_marcado = contar_accesibles(mapa)
    print("Mapa marcado (los '@' accesibles se muestran como 'x'):\n")
    imprimir_mapa(mapa_marcado)
    print(f"\nTotal de rollos accesibles: {total}")
