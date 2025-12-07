#!/usr/bin/env python3
# Day 6: Trash Compactor — solver

def read_grid(path="input.txt"):
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    # Igualar longitudes rellenando con espacios
    width = max(len(ln) for ln in lines)
    grid = [ln.ljust(width) for ln in lines]
    return grid, width, len(lines)


def is_separator_col(grid, col):
    """Una columna separadora es aquella que contiene SOLO espacios."""
    return all(row[col] == " " for row in grid)


def extract_problems(grid, width, height):
    """Devuelve una lista de problemas. Cada problema es (columnas_izq, columnas_der)."""
    problems = []
    in_problem = False
    start = None

    for c in range(width):
        sep = is_separator_col(grid, c)

        if sep:
            if in_problem:
                problems.append((start, c - 1))
                in_problem = False
        else:
            if not in_problem:
                start = c
                in_problem = True

    if in_problem:
        problems.append((start, width - 1))

    return problems


def parse_problem(grid, height, col_start, col_end):
    """
    De un bloque de columnas saca:
    - los números (uno por fila, excepto la última fila)
    - el operador '+' o '*' de la última fila
    """
    numbers = []
    for r in range(height - 1):
        segment = grid[r][col_start:col_end + 1]
        cleaned = segment.strip()
        if cleaned != "":
            numbers.append(int(cleaned))

    op_seg = grid[height - 1][col_start:col_end + 1].strip()
    if op_seg not in ["+", "*"]:
        raise ValueError(f"Operador inválido en columnas {col_start}-{col_end}: {op_seg}")

    return numbers, op_seg


def evaluate(numbers, op):
    if op == "+":
        return sum(numbers)
    else:
        result = 1
        for n in numbers:
            result *= n
        return result


def solve_day6():
    grid, width, height = read_grid("input.txt")
    problems_cols = extract_problems(grid, width, height)

    total = 0
    for (cs, ce) in problems_cols:
        nums, op = parse_problem(grid, height, cs, ce)
        total += evaluate(nums, op)

    return total


if __name__ == "__main__":
    print(solve_day6())
