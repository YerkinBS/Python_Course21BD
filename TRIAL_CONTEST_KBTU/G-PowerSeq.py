n = int(input())
v = []
for i in range(n):
    v.append(int(input()))

s = ''
num = 1
while len(s) < max(v):
    s += str(num)
    num *= 10

for i in v:
    print(s[i-1], end=' ')