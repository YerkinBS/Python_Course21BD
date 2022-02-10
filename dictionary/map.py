def sqr(x):
    return(x * x)

v = [1, 2, 3, 4, 5, 6]
l = list(map(sqr, v))
print(l)

s = list(map(int, input().split()))
print(s)