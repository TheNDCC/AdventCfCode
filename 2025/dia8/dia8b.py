#!/usr/bin/env python3
# day8_junctions.py
# Lee input.txt (cada línea "X,Y,Z") y resuelve:
# - Parte 1: tras conectar las 1000 parejas más cercanas, multiplicar las 3 mayores componentes.
# - Parte 2: multiplicar las X de los dos nodos que realizan la última unión necesaria para unir todo.

import sys
from itertools import combinations
from math import prod

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1]*n
        self.components = n

    def find(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        # union by size
        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        self.sz[ra] += self.sz[rb]
        self.components -= 1
        return True

    def comp_size(self, a):
        return self.sz[self.find(a)]

def read_points(path="input.txt"):
    pts = []
    with open(path, "r", encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if not ln:
                continue
            parts = ln.split(",")
            if len(parts) != 3:
                raise ValueError(f"Línea inválida: {ln}")
            x,y,z = map(int, parts)
            pts.append((x,y,z))
    return pts

def build_all_edges_sq(pts):
    n = len(pts)
    edges = []
    # Para reducir memoria en casos razonables, construimos como lista de tuplas (dist2,i,j)
    for i in range(n):
        xi, yi, zi = pts[i]
        for j in range(i+1, n):
            xj, yj, zj = pts[j]
            dx = xi - xj
            dy = yi - yj
            dz = zi - zj
            d2 = dx*dx + dy*dy + dz*dz
            edges.append((d2, i, j))
    return edges

def part1_multiply_top3_after_k_edges(pts, edges_sorted, k=1000):
    n = len(pts)
    dsu = DSU(n)
    # tomar primeras k edges (o menos si no hay suficientes)
    upto = min(k, len(edges_sorted))
    for idx in range(upto):
        _, i, j = edges_sorted[idx]
        dsu.union(i, j)
    # calcular tamaños por representante
    sizes = {}
    for i in range(n):
        r = dsu.find(i)
        sizes[r] = sizes.get(r, 0) + 1
    sizes_list = sorted(sizes.values(), reverse=True)
    # multiplicar las tres mayores (si menos de 3, multiplicar las existentes)
    top3 = sizes_list[:3]
    # si hay menos de 3 componentes, completar con 1 para que la multiplicación sea correcta
    while len(top3) < 3:
        top3.append(1)
    return top3[0] * top3[1] * top3[2]

def part2_last_union_x_product(pts, edges_sorted):
    n = len(pts)
    dsu = DSU(n)
    last_pair = None
    for d2, i, j in edges_sorted:
        merged = dsu.union(i, j)
        if merged:
            # si ahora components == 1, esta fue la última unión necesaria
            if dsu.components == 1:
                last_pair = (i, j)
                break
    if last_pair is None:
        raise RuntimeError("No se pudo unir todo el grafo (probablemente solo 0 o 1 punto).")
    xi = pts[last_pair[0]][0]
    xj = pts[last_pair[1]][0]
    return xi * xj

def main():
    pts = read_points("input.txt")
    n = len(pts)
    if n < 2:
        print("0")
        return
    # construir todas las aristas (dist^2, i, j)
    edges = build_all_edges_sq(pts)
    # ordenar por distancia (asc)
    edges.sort(key=lambda e: e[0])
    # Parte 1
    resultado1 = part1_multiply_top3_after_k_edges(pts, edges, k=1000)
    # Parte 2
    resultado2 = part2_last_union_x_product(pts, edges)
    print(resultado1)
    print(resultado2)

if __name__ == "__main__":
    main()
