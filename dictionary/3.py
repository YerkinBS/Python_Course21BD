d, n = {}, int(input())

for i in range(n):
    name, course = input().split()
    
    if course not in d.keys():
        d[course] = [name]
    else:
        d[course].append(name)


for key, value in sorted(d.items()):
    print(key, 'course :', end=' ')
    for i in range(len(value)):
        # print(value[i] + ', ' if i != len(value) - 1 else value[i], end='')
        if i != len(value) - 1:
            print(value[i] + ', ', end='')
        else:
            print(value[i])


# Input:
# 4
# Inara 1
# Yerkin 2
# Zarina 1
# Nurtay 2

# Output:
# 1 course : Inara, Zarina
# 2 course : Yerkin, Nurtay