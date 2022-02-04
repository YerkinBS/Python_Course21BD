c = input()
for i in range(0, len(c), 3):
    print(chr(int(c[i: i + 3])), end='')