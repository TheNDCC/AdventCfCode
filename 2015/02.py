fp = open ("input.txt", "r")

dimensiones_caja = fp.readlines()
fp.close()

def answer1():
    length_l, width_w, height_h = [], [], []
    lado = 0
    for caja in dimensiones_caja:
        
        aux = caja.strip()
        aux2 = aux.split("x")

        length_l.append(int(aux2[0]))
        width_w.append(int(aux2[1]))
        height_h.append(int(aux2[2]))

        area = 0

    for i in range(len(dimensiones_caja)):
        area = area + (2*length_l[i]*width_w[i] + 2*width_w[i]*height_h[i] + 2*height_h[i]*length_l[i])
    
        lado = lado + min([length_l[i]*width_w[i], width_w[i]*height_h[i], height_h[i]*length_l[i]])
    return  area+lado

def answer2():
    dimensiones = list(map(int, caja.strip().split("x")))  # Convertimos las dimensiones a enteros
        l, w, h = dimensiones
    return  

print(answer1())
print(answer2())