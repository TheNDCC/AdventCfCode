def max_subsequence_of_length_k(s: str, k: int) -> str:
    """
    Devuelve la subsecuencia (manteniendo orden) de longitud k
    que forma el mayor número posible. Implementación O(n) con pila.
    s: cadena de dígitos
    k: longitud objetivo (aquí 12)
    """
    n = len(s)
    if k > n:
        raise ValueError(f"La línea tiene longitud {n} < {k}; no se puede elegir {k} dígitos")

    to_remove = n - k  # cuántos dígitos podemos quitar
    stack = []

    for ch in s:
        # mientras podamos quitar y el último dígito en stack sea menor
        # que el actual, lo quitamos para obtener un número mayor
        while to_remove and stack and stack[-1] < ch:
            stack.pop()
            to_remove -= 1
        stack.append(ch)

    # si queda por quitar (caso decreciente), recortamos desde el final
    if to_remove:
        stack = stack[:-to_remove]

    # tomar exactamente k dígitos
    result = ''.join(stack[:k])
    return result


def sumar_joltages_por_banco(lines, k=12):
    """
    Para cada línea de dígitos (un banco), toma la subsecuencia máxima de longitud k,
    la interpreta como entero y suma todas.
    Devuelve (suma_total, lista_de_valores_por_linea) para comodidad.
    """
    total = 0
    valores = []
    for idx, line in enumerate(lines, start=1):
        s = line.strip()
        if not s:
            continue
        mayor_str = max_subsequence_of_length_k(s, k)
        mayor_int = int(mayor_str)
        valores.append((idx, mayor_str, mayor_int))
        total += mayor_int
    return total, valores


if __name__ == "__main__":
    # Leer input.txt (cada banco en una línea)
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    suma, detalles = sumar_joltages_por_banco(lines, k=12)

    for idx, sstr, sval in detalles:
        print(f"Banco {idx}: {sstr}  ({sval})")

    print("\nSuma total de joltages:", suma)
