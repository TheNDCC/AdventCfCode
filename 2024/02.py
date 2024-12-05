fp = open ("input.txt", "r")

puzzle_input = fp.readlines()
fp.close()

def check_report(report):
    aumenta = int(report[0]) > int(report[1])
    for i in range(len(report)-1):
        result = abs(int(report[i]) - int(report[i + 1]))
        if result < 1 or result > 3:
            return False
        if (int(report[i]) > int(report[i+1])) != aumenta:
            return False
    
    return True

def answer1():
    count = 0
    for report in puzzle_input:   
        report = report.strip().split(" ")
        
        count += 1
        aumenta = int(report[0]) > int(report[1])
        for i in range(len(report)-1):
            result = abs(int(report[i]) - int(report[i + 1]))
            if result < 1 or result > 3:
                count -= 1
                break
            if (int(report[i]) > int(report[i+1])) != aumenta:
                count -= 1
                break
    return count
def answer2():
    count = 0
    for report in puzzle_input:
        report = report.strip().split(" ")
        if check_report(report):
            count +=1
            print(report)
            continue
        for n in range(len(report)):
            backup = report[n]
            #print(f"antes de borrar:{report}")
            del report[n]
            #print(f"borrando:{report}")
            if check_report(report):
                count += 1
            report.insert(n,backup)
    return count

print(answer1())
print(answer2())