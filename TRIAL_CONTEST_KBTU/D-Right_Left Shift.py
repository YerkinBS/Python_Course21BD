v = list(map(int, input().split()))
com = input().split()
if com[0] == 'L': print(*v[int(com[1]):] + v[:int(com[1])])
else: print(*v[int(com[1]) + 1:] + v[:int(com[1]) + 1])