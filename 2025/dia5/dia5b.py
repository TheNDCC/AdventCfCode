#!/usr/bin/env python3
# day5_part2.py
# Lee input.txt (rangos en líneas hasta la primera línea vacía) y devuelve
# la cantidad total de IDs distintos que están considerados "fresh" por los rangos.

from typing import List, Tuple

def parse_ranges(path="input.txt") -> List[Tuple[int,int]]:
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    # tomar hasta la primera línea vacía
    ranges_lines = []
    for ln in lines:
        if ln == "":
            break
        # permitir múltiples rangos en la misma línea separados por comas
        parts = [p.strip() for p in ln.split(",") if p.strip()]
        for p in parts:
            if "-" not in p:
                continue
            a,b = p.split("-", 1)
            ranges_lines.append((int(a), int(b)))
    return ranges_lines

def merge_ranges(ranges: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
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

def total_covered_ids(merged: List[Tuple[int,int]]) -> int:
    total = 0
    for s,e in merged:
        # cada rango es inclusivo
        total += (e - s + 1)
    return total

if __name__ == "__main__":
    ranges = parse_ranges("input.txt")
    merged = merge_ranges(ranges)
    result = total_covered_ids(merged)
    print(result)
