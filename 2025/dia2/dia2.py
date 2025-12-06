def parse_ranges(text):
    """
    Recibe el contenido del archivo como texto y devuelve
    una lista de tuplas (inicio, fin).
    """
    # Quitar saltos de línea y espacios
    text = text.replace("\n", "").strip()
    if not text:
        return []

    parts = [p for p in text.split(",") if p]  # ignorar vacíos
    ranges = []
    for p in parts:
        a_str, b_str = p.split("-")
        ranges.append((int(a_str), int(b_str)))
    return ranges


def generar_ids_invalidos(max_id):
    """
    Genera todos los números de la forma X repetido dos veces (sin ceros a la izquierda)
    que sean <= max_id.
    """
    invalid_ids = []
    max_len = len(str(max_id))

    # La longitud total del número es 2 * len(X)
    for half_len in range(1, max_len // 2 + 1):
        start = 10 ** (half_len - 1)      # evita ceros a la izquierda
        end = 10 ** half_len - 1

        for h in range(start, end + 1):
            s = str(h)
            rep = int(s + s)              # X repetido dos veces
            if rep > max_id:
                break                     # ya no tiene sentido seguir para esta longitud
            invalid_ids.append(rep)

    return invalid_ids


def suma_ids_invalidos(ranges):
    """
    Dada una lista de rangos (a, b), calcula la suma de todos los IDs inválidos
    que caen en esos rangos.
    """
    if not ranges:
        return 0

    max_id = max(b for _, b in ranges)
    invalid_ids = generar_ids_invalidos(max_id)

    total = 0
    for a, b in ranges:
        for v in invalid_ids:
            if a <= v <= b:
                total += v
    return total


if __name__ == "__main__":
    # Leer todo el archivo (una sola línea muy larga en el input real)
    with open("input.txt", "r", encoding="utf-8") as f:
        content = f.read()

    ranges = parse_ranges(content)
    resultado = suma_ids_invalidos(ranges)

    print("La suma de todos los IDs inválidos es:", resultado)
