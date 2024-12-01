f = open("input.txt", "r")
read = f.read()


def answer1():
    floor = 0
    for i in range(len(read)):
        
        if read[i] == "(":
            floor += 1

        elif read[i] ==")":
            floor -= 1
    return floor

def answer2():
    floor = 0
    for i in range(len(read)):
        
        if read[i] == "(":
            floor += 1

        elif read[i] ==")":
            floor -= 1

        if floor == -1:
            return i + 1
            

print(answer1())
print(answer2())
