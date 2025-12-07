#!/usr/bin/env python3
# day6_part2.py
# Lee input.txt y resuelve "cephalopod math" Part Two (leer columnas derecha->izquierda).

from typing import List

def read_grid(path="input.txt") -> List[List[str]]:
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    if not lines:
        return []
    width = max(len(ln) for ln in lines)
    # Pad lines with spaces to form a rectangular grid
    grid = [list(ln.ljust(width, " ")) for ln in lines]
    return grid

def find_separator_columns(grid: List[List[str]]) -> List[bool]:
    """Devuelve una lista booleana por columna: True si es columna separadora (todas espacios)."""
    if not grid:
        return []
    rows = len(grid)
    cols = len(grid[0])
    sep = []
    for c in range(cols):
        all_space = True
        for r in range(rows):
            if grid[r][c] != " ":
                all_space = False
                break
        sep.append(all_space)
    return sep

def split_blocks_by_columns(sep_cols: List[bool]) -> List[tuple]:
    """
    Dado el vector de columnas separadoras, devuelve lista de (start_col, end_col)
    para bloques contiguos de columnas no-separadoras. end_col inclusive.
    """
    blocks = []
    c = 0
    n = len(sep_cols)
    while c < n:
        # skip separators
        while c < n and sep_cols[c]:
            c += 1
        if c >= n:
            break
        start = c
        while c < n and not sep_cols[c]:
            c += 1
        end = c - 1
        blocks.append((start, end))
    return blocks

def column_number_from_grid(grid: List[List[str]], col: int, op_row: int) -> str:
    """
    Construye la cadena numérica de la columna `col` leyendo de fila 0 .. op_row-1
    y concatenando solo dígitos (ignorando espacios). Devuelve '' si no hay dígitos.
    """
    digits = []
    for r in range(op_row):
        ch = grid[r][col]
        if ch.isdigit():
            digits.append(ch)
    return "".join(digits)

def evaluate_problem(grid: List[List[str]], block: tuple) -> int:
    """
    Evalúa un único bloque (start_col, end_col).
    Para Part Two: leer columnas de derecha a izquierda; cada columna produce un número
    concatenando dígitos top->bottom (filas 0..op_row-1). El operador está en la fila op_row
    (última fila) en alguna columna del bloque; tomamos el primer char no-espacio en esa fila.
    """
    start, end = block
    rows = len(grid)
    op_row = rows - 1
    # hallar operador: primera celda no-espacio en la fila inferior dentro del bloque
    op = None
    for c in range(start, end + 1):
        ch = grid[op_row][c]
        if ch in "+*":
            op = ch
            break
    if op is None:
        # si no se encuentra operador explícito, intentar cualquier no-espacio (defensivo)
        for c in range(start, end + 1):
            ch = grid[op_row][c]
            if ch.strip():
                op = ch.strip()
                break
    if op is None:
        raise ValueError(f"No se encontró operador en el bloque columnas {start}-{end}")

    # Recolectar números leyendo columnas de derecha a izquierda
    numbers = []
    for c in range(end, start - 1, -1):
        num_str = column_number_from_grid(grid, c, op_row)
        if num_str != "":
            numbers.append(int(num_str))

    if not numbers:
        return 0

    if op == "+":
        return sum(numbers)
    elif op == "*":
        prod = 1
        for v in numbers:
            prod *= v
        return prod
    else:
        raise ValueError(f"Operador desconocido '{op}' en columnas {start}-{end}")

def main():
    grid = read_grid("input.txt")
    if not grid:
        print(0)
        return

    sep_cols = find_separator_columns(grid)
    blocks = split_blocks_by_columns(sep_cols)

    grand_total = 0
    for blk in blocks:
        val = evaluate_problem(grid, blk)
        grand_total += val

    print(grand_total)

if __name__ == "__main__":
    main()
