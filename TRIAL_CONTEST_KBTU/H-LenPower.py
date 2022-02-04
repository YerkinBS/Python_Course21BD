def check(x):
    i = 0
    while True:
        if 2 ** i == len(x): return 'YES'
        if 2 ** i > len(x): return 'NO'
        i += 1

n = input().split()
for i in n: print(check(i), end= ' ')