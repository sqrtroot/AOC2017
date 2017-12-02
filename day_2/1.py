print(sum(map(lambda x: max(x)-min(x), map(lambda x: tuple(map(lambda y: int(y), x.split())), open('code.txt').readlines()))))
