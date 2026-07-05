n = int(input())
lst = []
flag = True
for i in range(n):
    s = input()
    s = s.split()
    s = list(map(int, s))
    if sum(s) % 2 != 0:
        flag = False
        break
    lst.append(s)
if flag == False:
    print("NO")
else:
    for i in range(n):
        suma = 0
        for j in range(n):
            suma += lst[i][j]
        if suma % 2 != 0:
            flag = False
            break
    if flag == False:
        print("NO")
    else:
        print("YES")