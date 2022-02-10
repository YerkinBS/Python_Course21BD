from sympy import re


n = int(input())
v = list()
d = dict()

for i in range(n):
    v += input().split()

for i in v:
    for j in i:
        if j not in d.keys(): d[j] = 1
        else: d[j] += 1

for value in sorted(d.values(), key=int, reverse=True):
    for key in d.keys():
        if d[key] == value: print(key, ' : ', value)