def solution(args):
    lst = [args[0]]
    s = ''
    rez_s = ''
    args.append(0)
    print(args)
    for i in range(1, len(args)):
        if len(lst) == 0 or args[i] - args[i - 1] == 1:
            lst.append(args[i])
        else:
            if len(lst) >= 3:
                s = f'{lst[0]}-{lst[-1]},'
                rez_s += s
            else:
                rez_s += str(lst[0]) + ','
                if len(lst) == 2:
                    rez_s += str(lst[1]) + ','
            lst = [args[i]]
    return rez_s[0:-1]
print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))

