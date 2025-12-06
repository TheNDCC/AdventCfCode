def parte1(rotaciones):
    """
    Cuenta cuántas veces la esfera termina exactamente en 0
    después de una rotación completa.
    """
    pos = 50
    cuenta_ceros = 0

    for linea in rotaciones:
        linea = linea.strip()
        if not linea:
            continue

        dir_ = linea[0]
        pasos = int(linea[1:])

        if dir_ == 'L':
            pos = (pos - pasos) % 100
        elif dir_ == 'R':
            pos = (pos + pasos) % 100
        else:
            raise ValueError(f"Instrucción inválida: {linea}")

        if pos == 0:
            cuenta_ceros += 1

    return cuenta_ceros


def ceros_durante_rotacion(pos_inicial, dir_, pasos):
    """
    Cuenta cuántas veces se pasa por 0 DURANTE los clics de una sola rotación,
    sin simular clic por clic (funciona incluso si pasos es enorme).
    Devuelve: (n_ceros_en_esta_rotacion, nueva_posicion)
    """
    s = pos_inicial  # posición inicial
    N = pasos

    if dir_ == 'R':
        # R: pos_k = (s + k) mod 100
        # Queremos (s + k) ≡ 0 (mod 100) -> k ≡ -s (mod 100)
        first_k = (-s) % 100
    elif dir_ == 'L':
        # L: pos_k = (s - k) mod 100
        # (s - k) ≡ 0 -> k ≡ s (mod 100)
        first_k = s % 100
    else:
        raise ValueError(f"Dirección inválida: {dir_}")

    # Los "clics" empiezan en k = 1, así que si first_k == 0,
    # el primer 0 es en k = 100 (una vuelta completa).
    if first_k == 0:
        first_k = 100

    if first_k > N:
        hits = 0
    else:
        # Luego de first_k, volvemos a pasar por 0 cada 100 pasos.
        hits = 1 + (N - first_k) // 100

    # Actualizamos la posición final después de N pasos
    if dir_ == 'R':
        nueva_pos = (s + N) % 100
    else:  # 'L'
        nueva_pos = (s - N) % 100

    return hits, nueva_pos


def parte2(rotaciones):
    """
    Método 0x434C49434B:
    Cuenta cuántas veces CADA CLIC hace que la esfera apunte a 0.
    """
    pos = 50
    total_ceros = 0

    for linea in rotaciones:
        linea = linea.strip()
        if not linea:
            continue

        dir_ = linea[0]
        pasos = int(linea[1:])

        ceros_en_esta, pos = ceros_durante_rotacion(pos, dir_, pasos)
        total_ceros += ceros_en_esta

    return total_ceros


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Parte 1 (por si quieres verificar lo de antes)
    p1 = parte1(lines)
    print("Parte 1 - contraseña (finales en 0):", p1)

    # Parte 2 (método 0x434C49434B)
    p2 = parte2(lines)
    print("Parte 2 - contraseña (clics en 0):", p2)
