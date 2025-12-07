#!/usr/bin/env python3
# day5_cafeteria.py
# Lee input.txt (rangos, línea vacía, ids) y cuenta cuántos ids están en algún rango.

from bisect import bisect_right

def parse_input(path="input.txt"):
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    # separar en dos partes por la primera línea vacía
    try:
        sep = lines.index('')
        range_lines = lines[:sep]
        id_lines = lines[sep+1:]
    except ValueError:
        # si no hay línea vacía, asumimos todo son rangos y no hay ids
        range_lines = lines
        id_lines = []
    ranges = []
    for r in range_lines:
        if not r: continue
        a,b = r.split("-")
        ranges.append((int(a), int(b)))
    ids = [int(x) for x in id_lines if x]
    return ranges, ids

def merge_ranges(ranges):
    """Une rangos solapados y devuelve lista ordenada de (start,end)."""
    if not ranges:
        return []
    ranges_sorted = sorted(ranges, key=lambda x: (x[0], x[1]))
    merged = []
    cur_s, cur_e = ranges_sorted[0]
    for s,e in ranges_sorted[1:]:
        if s <= cur_e + 1:  # solapan o son contiguos
            if e > cur_e:
                cur_e = e
        else:
            merged.append((cur_s, cur_e))
            cur_s, cur_e = s, e
    merged.append((cur_s, cur_e))
    return merged

def is_id_fresh(merged_ranges, x):
    """
    Comprueba si x está dentro de algún rango en merged_ranges.
    Usamos bisect sobre los inicios para localizar candidato.
    """
    if not merged_ranges:
        return False
    starts = [r[0] for r in merged_ranges]
    i = bisect_right(starts, x) - 1
    if i < 0:
        return False
    s,e = merged_ranges[i]
    return s <= x <= e

def count_fresh_ids(ranges, ids):
    merged = merge_ranges(ranges)
    # para eficiencia, preextraer starts (opcional dentro is_id_fresh)
    starts = [r[0] for r in merged]
    from bisect import bisect_right
    cnt = 0
    for x in ids:
        i = bisect_right(starts, x) - 1
        if i >= 0 and merged[i][0] <= x <= merged[i][1]:
            cnt += 1
    return cnt

if __name__ == "__main__":
    ranges, ids = parse_input("input.txt")
    result = count_fresh_ids(ranges, ids)
    print(result)
