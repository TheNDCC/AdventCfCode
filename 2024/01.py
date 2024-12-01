fp = open ("input.txt", "r")

puzzle_input = fp.readlines()
fp.close()

def answer1():
    lista_a, lista_b = [], []
    distancia = []
    
    for line in puzzle_input:   
        line = line.strip().split("   ")
        lista_a.append(int(line[0]))
        lista_b.append(int(line[1]))

    lista_a.sort()
    lista_b.sort()
    
    for i in range(len(lista_a)):
            
        distancia.append(abs(lista_b[i]-lista_a[i]))
        
    distancia = sum(distancia)
    
    return distancia

def answer2():
    lista_a, lista_b = [], []
    distancia = []
    
    for line in puzzle_input:   
        line = line.strip().split("   ")
        lista_a.append(int(line[0]))
        lista_b.append(int(line[1]))

    lista_a.sort()
    lista_b.sort()
    
    for i in range(len(lista_a)):
            
        distancia.append(abs(lista_a[i]*lista_b.count(lista_a[i])))
        
    distancia = sum(distancia)
    
    return distancia

print(answer1())
print(answer2())
