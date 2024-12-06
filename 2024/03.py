import re

fp = open ("input.txt", "r")

puzzle_input = fp.read()
fp.close()

def answer1():
    x = re.findall("mul\\(([0-9]+),([0-9]+)\\)", puzzle_input)
    resultado = 0
    for mul in x:
        resultado += int(mul[0])*int(mul[1])
        #print(mul)
    return resultado
def answer2():
    #x = puzzle_input.replace("\n","")
    #x = puzzle_input.replace(" ","")
    x = puzzle_input
    x = re.sub(r'don\'t\(\)[\s\S]*?(do\(\))', '', x)
    x = re.findall("mul\\(([0-9]+),([0-9]+)\\)", x)
    contar = 0
    resultado = 0
    for mul in x:
        resultado += int(mul[0])*int(mul[1])
        #print(mul)
        contar += 1
    print(contar)
    return resultado

print(answer1())
print(answer2())