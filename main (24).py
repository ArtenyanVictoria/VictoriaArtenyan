# s1 = input()
# s2 = input()
# kol = 0
# maxi = 0
# s = ''
# ss = ''
# for i in range(len(s1)):
#     if s1[i] in s2:
#         for j in range(i + 1, len(s1)):
#             if s1[i: j + 1] in s2:
#                 kol = len(s1[i: j + 1])
#                 s = s1[i: j + 1]
#                 if kol > maxi:
#                     maxi = kol
#                     ss = s1[i: j + 1]
# print(maxi)

# n = int(input())
# lst = []
# ls = [0] # Где мы изначально находимся 0 - A, 1 - B и т. д. ls - храним где мы были и находимся
# suma = 0 # Итоговая сумма
# # Обрабатывем входные данные, предворительно заменяня нули на максимальное возможное число
# for i in range(n):
#     s = ' ' + input() + ' '
#     s = s.replace(' 0 ', ' ' + str(2 ** 31 - 1) + ' ')
#     s = s.split()
#     s = list(map(int, s))
#     lst.append(s)
# # Пробегаемся по внутренностям ls. d - где мы сейчас находимся
# for i in range(0, n):
#     d = ls[i]
#     # Пробегаемсяя по элементам lst[d]
#     for j in range(0, n):
#         if lst[d][j] == min(lst[d]) and j not in ls:
#             ls.append(j)
#             suma += min(lst[d])
#             break
#         elif lst[d][j] == min(lst[d]) and j in ls:
#             pst = lst[d].copy()
#             pst.sort()
#             for k in range(len(pst)):
#                 flag = False
#                 for l in range(len(pst)):
#                     if pst[k] == lst[d][l] and l not in ls:
#                         ls.append(l)
#                         suma += pst[k]
#                         flag = True
#                         break
#                 if flag == True:
#                     break
# print(suma)

# def matrix_mult(a, b):
#     return [
#         [
#             a[0][0] * b[0][0] + a[0][1] * b[1][0] + a[0][2] * b[2][0] + a[0][3] * b[3][0],
#             a[0][0] * b[0][1] + a[0][1] * b[1][1] + a[0][2] * b[2][1] + a[0][3] * b[3][1],
#             a[0][0] * b[0][2] + a[0][1] * b[1][2] + a[0][2] * b[2][2] + a[0][3] * b[3][2],
#             a[0][0] * b[0][3] + a[0][1] * b[1][3] + a[0][2] * b[2][3] + a[0][3] * b[3][3],
#         ],
#         [
#             a[1][0] * b[0][0] + a[1][1] * b[1][0] + a[1][2] * b[2][0] + a[1][3] * b[3][0],
#             a[1][0] * b[0][1] + a[1][1] * b[1][1] + a[1][2] * b[2][1] + a[1][3] * b[3][1],
#             a[1][0] * b[0][2] + a[1][1] * b[1][2] + a[1][2] * b[2][2] + a[1][3] * b[3][2],
#             a[1][0] * b[0][3] + a[1][1] * b[1][3] + a[1][2] * b[2][3] + a[1][3] * b[3][3],
#         ],
#         [
#             a[2][0] * b[0][0] + a[2][1] * b[1][0] + a[2][2] * b[2][0] + a[2][3] * b[3][0],
#             a[2][0] * b[0][1] + a[2][1] * b[1][1] + a[2][2] * b[2][1] + a[2][3] * b[3][1],
#             a[2][0] * b[0][2] + a[2][1] * b[1][2] + a[2][2] * b[2][2] + a[2][3] * b[3][2],
#             a[2][0] * b[0][3] + a[2][1] * b[1][3] + a[2][2] * b[2][3] + a[2][3] * b[3][3],
#         ],
#         [
#             a[3][0] * b[0][0] + a[3][1] * b[1][0] + a[3][2] * b[2][0] + a[3][3] * b[3][0],
#             a[3][0] * b[0][1] + a[3][1] * b[1][1] + a[3][2] * b[2][1] + a[3][3] * b[3][1],
#             a[3][0] * b[0][2] + a[3][1] * b[1][2] + a[3][2] * b[2][2] + a[3][3] * b[3][2],
#             a[3][0] * b[0][3] + a[3][1] * b[1][3] + a[3][2] * b[2][3] + a[3][3] * b[3][3],
#         ],
#     ]
#
# def matrix_pow(mat, power):
#     result = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
#     while power > 0:
#         if power % 2 != 0:
#             result = matrix_mult(result, mat)
#         mat = matrix_mult(mat, mat)
#         power //= 2
#     return result
#
# def count_paths(n):
#     if n == 0:
#         return 1
#     transition = [
#         [0, 1, 1, 1],
#         [1, 0, 1, 1],
#         [1, 1, 0, 1],
#         [1, 1, 1, 0],
#     ]
#     mat = matrix_pow(transition, n)
#     return mat[0][0]
#
# n = int(input())
# print(count_paths(n))

# def solve():
#     n, m = map(int, input().split())
#     houses = list(map(int, input().split()))
#
#     # cost[i][j] — минимальная сумма, если покрыть дома i..j одной точкой
#     cost = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(i, n):
#             median = houses[(i + j) // 2]
#             total = 0
#             for k in range(i, j + 1):
#                 total += abs(houses[k] - median)
#             cost[i][j] = total
#
#     # DP[k][l] — минимальная сумма для первых l домов и k точек
#     INF = float('inf')
#     dp = [[INF] * (n + 1) for _ in range(m + 1)]
#     parent = [[-1] * (n + 1) for _ in range(m + 1)]
#     dp[0][0] = 0
#
#     for k in range(1, m + 1):
#         for l in range(1, n + 1):
#             for prev_l in range(0, l):
#                 if dp[k - 1][prev_l] + cost[prev_l][l - 1] < dp[k][l]:
#                     dp[k][l] = dp[k - 1][prev_l] + cost[prev_l][l - 1]
#                     parent[k][l] = prev_l
#
#     print(dp[m][n])
#
#     # Восстановление ответа
#     res = []
#     current_l = n
#     for k in range(m, 0, -1):
#         prev_l = parent[k][current_l]
#         # Точка для домов prev_l..current_l-1
#         median_pos = (prev_l + current_l - 1) // 2
#         res.append(houses[median_pos])
#         current_l = prev_l
#     res.sort()
#     print(' '.join(map(str, res)))
#
#
# solve()
