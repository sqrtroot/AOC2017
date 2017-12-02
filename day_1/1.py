print((lambda number: sum(map(int,[number[i] if number[i] == number[(i+1)%len(number)] else "0" for i in range(len(number))])))(open("day_1/code.txt").read()))
