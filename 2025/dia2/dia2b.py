def parse_ranges(text):
    """
    Recibe el contenido del archivo como texto y devuelve
    una lista de tuplas (inicio, fin).
    """
    text = text.replace("\n", "").strip()
    if not text:
        return []

    parts = [p for p in text.split(",") if p]  # ignorar vacíos
    ranges = []
    for p in parts:
        a_str, b_str = p.split("-")
        ranges.append((int(a_str), int(b_str)))
    return ranges


def generar_ids_invalidos_repetidos(max_id):
    """
    Genera todos los números de la forma X repetido k veces (k >= 2),
    sin ceros a la izquierda, que sean <= max_id.
    """
    invalid_ids = set()
    max_len = len(str(max_id))

    # bloque de longitud block_len, repetido k veces
    for block_len in range(1, max_len):  # longitud total >= 2, así que block_len < max_len
        start = 10 ** (block_len - 1)      # evita ceros a la izquierda
        end = 10 ** block_len - 1

        # número total de dígitos = block_len * k
        for k in range(2, max_len // block_len + 1):
            for block in range(start, end + 1):
                s = str(block) * k        # repetimos el bloque k veces
                if len(s) > max_len:
                    break                 # ya se pasó de la longitud máxima posible

                n = int(s)
                if n > max_id:
                    break                 # para este k, números siguientes serán mayores

                invalid_ids.add(n)

    return sorted(invalid_ids)


def suma_ids_invalidos(ranges):
    """
    Dada una lista de rangos (a, b), calcula la suma de todos los IDs inválidos
    (bloque repetido >= 2 veces) que caen en esos rangos.
    """
    if not ranges:
        return 0

    max_id = max(b for _, b in ranges)
    invalid_ids = generar_ids_invalidos_repetidos(max_id)

    total = 0
    for a, b in ranges:
        for v in invalid_ids:
            if v > b:
                break
            if v >= a:
                total += v
    return total


if __name__ == "__main__":
    # Leer el archivo con los rangos
    with open("input.txt", "r", encoding="utf-8") as f:
        content = f.read()

    ranges = parse_ranges(content)
    resultado = suma_ids_invalidos(ranges)

    print("La suma de todos los IDs inválidos (parte 2) es:", resultado)
