#!/usr/bin/env python3
# day7_laboratories.py
# Lee "input.txt", simula los haces y cuenta cuántas veces se produce un split ('^').

from collections import deque

def read_grid(path="input.txt"):
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    return lines

def find_start(grid):
    for i, row in enumerate(grid):
        j = row.find('S')
        if j != -1:
            return i, j
    raise ValueError("No se encontró 'S' en el input")

def count_splits(grid):
    n = len(grid)
    if n == 0:
        return 0
    m = max(len(row) for row in grid)
    # Asegurar que todas las filas tengan mismo ancho (rellenar con espacios)
    grid = [row.ljust(m, ' ') for row in grid]

    sr, sc = find_start(grid)
    # columnas con haces en la fila anterior (inicialmente la columna de S)
    current_cols = {sc}
    splits = 0

    # procesar fila a fila hacia abajo empezando en la fila siguiente a S
    for r in range(sr + 1, n):
        # columnas de haces que llegan a esta fila (inicialmente las que vienen de arriba)
        cols = set(c for c in current_cols if 0 <= c < m)
        if not cols:
            break

        # En la misma fila, un split puede generar haces a izquierda/derecha que a su vez
        # pueden caer sobre más spliters en la misma fila. Iteramos hasta estabilizar.
        while True:
            new_cols = set(cols)
            changed = False
            for c in list(cols):
                if 0 <= c < m and grid[r][c] == '^':
                    # Este haz golpea un splitter: cuenta 1 split
                    splits += 1
                    # Este haz no continúa en c; en su lugar genera haces en c-1 y c+1
                    if c in new_cols:
                        new_cols.discard(c)
                    # añadir izquierda y derecha si dentro de límites
                    if c - 1 >= 0:
                        if c - 1 not in new_cols:
                            new_cols.add(c - 1)
                            changed = True
                    if c + 1 < m:
                        if c + 1 not in new_cols:
                            new_cols.add(c + 1)
                            changed = True
                    # note: removing c already considered a change as well
                    if c in cols:
                        # removing c may be a change if not already removed
                        if c in new_cols:
                            pass
                        else:
                            changed = True
            # si no hubo cambios, ya estabilizó
            if not changed:
                cols = new_cols
                break
            cols = new_cols

        # para la siguiente fila, los haces vienen de las mismas columnas (bajan un paso)
        # pero si alguna columna actual en esta fila es un splitter '^', debería haber sido
        # procesada y eliminado en la estabilización anterior, así que cols ya no contiene '^'
        # (salvo si los vecinos estaban fuera del rango y no se pudieron crear; en ese caso el haz
        # simplemente desaparece).
        # Filtrar columnas válidas y que no estén en un '^' (porque un haz no continúa desde '^').
        next_cols = set()
        for c in cols:
            if 0 <= c < m and grid[r][c] != '^' and grid[r][c] != ' ':
                # si es cualquier caracter distinto de '^' y no es espacio, el haz ocupa esa columna
                # y seguirá hacia abajo en la siguiente fila
                next_cols.add(c)
            else:
                # si es espacio ' ' o fuera de la rejilla, ese haz sale del manifold y no continúa
                if 0 <= c < m and grid[r][c] == ' ':
                    # no continua
                    pass
                else:
                    # si era '.', letras, etc., tratamos igual a '.': continúa
                    if 0 <= c < m and grid[r][c] == '.':
                        next_cols.add(c)
        current_cols = next_cols

        # si no quedan haces que continúen, terminamos
        if not current_cols:
            # pero aún podrían quedar splits in-row for the same r from beams that were created
            # but don't continue to next row; however those were already counted during stabilization.
            break

    return splits

if __name__ == "__main__":
    grid = read_grid("input.txt")
    result = count_splits(grid)
    print(result)
