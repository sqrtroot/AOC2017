print((lambda number: sum(map(int,[number[i] if number[i] == number[(i+int(len(number)/2))%len(number)] else "0" for i in range(len(number))])))(open("code.txt").read()))
