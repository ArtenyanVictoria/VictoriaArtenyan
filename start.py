s = '{это[какая - то]}билиберда)'
lst = []
flag = True
for i in range(len(s)):
    if s[i] == '(' or s[i] == '{' or s[i] == '[':
        lst.append(s[i])
    elif (s[i] == ')' and '(' in lst):
        lst.pop(lst.index('('))
    elif (s[i] == '}' and '{' in lst):
        lst.pop(lst.index('{'))
    elif (s[i] == ']' and '[' in lst):
        lst.pop(lst.index('['))
    elif (s[i] == ')' and '(' not in lst):
        flag = False
        break
    elif (s[i] == ']' and '[' not in lst):
        flag = False
        break
    elif (s[i] == '}' and '{' not in lst):
        flag = False
        break
if flag == True and len(lst) == 0:
    print(True)
if flag == False or len(lst) > 0:
    print(False)

