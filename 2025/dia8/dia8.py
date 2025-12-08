#!/usr/bin/env python3
# day8_part2.py
# Lee puntos 3D desde input.txt (una línea por punto "x,y,z"),
# toma las 1000 parejas con menor distancia euclidiana (si hay menos, todas),
# conecta en ese orden (union-find), y al final imprime el producto
# de los tamaños de las tres mayores componentes.

import itertools
import math
from collections import Counter

def read_points(path="input.txt"):
    pts = []
    with open(path, "r", encoding="utf-8") as f:
        for ln in f:
            s = ln.strip()
            if not s:
                continue
            parts = s.split(",")
            if len(parts) != 3:
                raise ValueError(f"Línea con formato inesperado: {s}")
            x,y,z = map(int, parts)
            pts.append((x,y,z))
    return pts

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
    def find(self, a):
        p = self.parent
        while p[a] != a:
            p[a] = p[p[a]]
            a = p[a]
        return a
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        # union by size
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True
    def component_sizes(self):
        # compress then count roots
        for i in range(len(self.parent)):
            self.parent[i] = self.find(i)
        cnt = Counter(self.parent)
        return [cnt[r] for r in cnt]

def squared_dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

def main():
    points = read_points("input.txt")
    n = len(points)
    if n < 2:
        print(0)
        return

    # Generar todas las parejas con su distancia al cuadrado
    # Para ahorrar memoria en caso muy grande, podemos usar nlargest/nsmallest,
    # pero para inputs típicos esto está bien.
    pairs = []
    for (i, p), (j, q) in itertools.combinations(enumerate(points), 2):
        d2 = squared_dist(p, q)
        pairs.append((d2, i, j))

    # ordenar por distancia creciente
    pairs.sort(key=lambda x: x[0])

    # tomar las primeras 1000 (o todas si hay menos)
    limit = min(1000, len(pairs))
    chosen = pairs[:limit]

    dsu = DSU(n)
    # aplicar las conexiones en el orden elegido
    for d2, i, j in chosen:
        dsu.union(i, j)

    sizes = dsu.component_sizes()
    sizes.sort(reverse=True)
    # si hay menos de 3 componentes, rellenar con 1s para multiplicar correctamente
    top3 = sizes[:3] + [1,1]
    product = top3[0] * top3[1] * top3[2]
    print(product)

if __name__ == "__main__":
    main()
