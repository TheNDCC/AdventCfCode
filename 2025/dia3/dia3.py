def max_joltage_for_bank(bank: str) -> int:
    """
    Dado un string de dígitos (un banco de baterías),
    devuelve el mayor número de dos dígitos que se puede formar
    eligiendo dos posiciones i < j (sin reordenar), en O(n) y O(1) memoria.
    """
    s = bank.strip()
    n = len(s)
    if n < 2:
        raise ValueError("Cada banco debe tener al menos dos baterías")

    best_second = -1   # mejor dígito visto a la derecha
    best_pair = -1     # mejor número de dos dígitos encontrado

    # Recorremos de derecha a izquierda
    for i in range(n - 1, -1, -1):
        d = int(s[i])

        # Si ya hay algún dígito a la derecha, podemos formar un par
        if best_second != -1:
            candidate = 10 * d + best_second
            if candidate > best_pair:
                best_pair = candidate

        # Actualizamos el mejor dígito para usar como segundo
        if d > best_second:
            best_second = d

    return best_pair


def total_output_joltage(lines):
    """
    Recibe una lista de líneas (bancos) y devuelve la suma
    de los máximos jolts de cada banco.
    """
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        total += max_joltage_for_bank(line)
    return total


if __name__ == "__main__":
    # Leer el archivo de entrada
    with open("input.txt", "r", encoding="utf-8") as f:
        banks = [line.strip() for line in f if line.strip()]

    total = total_output_joltage(banks)
    print("El total de output joltage es:", total)
