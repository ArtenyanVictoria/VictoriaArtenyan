import random
a = """1   2   3
4   x   6
7   8   9"""
print(a)
lst = ["1", "2", "3", "4", "6", "7", "8", "9"]
kol = 0
for i in range(8):
    if i == 0:
        while True:
            mystep = input()
            if mystep in lst:
                break
            else:
                print("Error")
                print("Try again")
        lst.remove(mystep)
        a = a.replace(mystep, "0")
        print(a)
        print("      ")
        m = random.choice(lst)
        lst.remove(m)
        a = a.replace(m, "x")
        print(a)
    else:
        if kol == 1:
            break
        while True:
            mystep = input()
            if mystep in lst:
                break
            else:
                print("Error")
                print("Try again")
        lst.remove(mystep)
        a = a.replace(mystep, "0")
        print(a)
        print("      ")
        if a[0] == a[4] == a[8] == "0" or a[0] == a[10] == a[20] == "0" or a[20] == a[24] == a[28] == "0" or a[8] == a[18] == a[28] == "0":
            print("You won!")
            kol += 1
            break
        m = random.choice(lst)
        lst.remove(m)
        a = a.replace(m, "x")
        print(a)
        if a[0] == a[14] == a[28] == "x" or a[0] == a[4] == a[8] == "x" or a[0] == a[10] == a[20] == "x" or a[10] == a[14] == a[18] == "x" or a[20] == a[24] == a[28] == "x" or a[4] == a[14] == a[24] == "x" or a[8] == a[18] == a[28] == "x" or a[8] == a[14] == a[20] == "x":
            print("You lose!")
            kol += 1
            break
        if len(lst) == 0 and (a[0] == a[14] == a[28] == "x" or a[0] == a[4] == a[8] == "x" or a[0] == a[10] == a[20] == "x" or a[10] == a[14] == a[18] == "x" or a[20] == a[24] == a[28] == "x" or a[4] == a[14] == a[24] == "x" or a[8] == a[18] == a[28] == "x"):
            print(a)
            print("You lose!")
            kol += 1
            break
        if len(lst) == 0:
            print("Draw")
            kol += 1
            break

