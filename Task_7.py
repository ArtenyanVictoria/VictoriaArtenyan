import sys
from collections import deque


def main():
    input = sys.stdin.read
    data = input().split()

    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1

    adj = [[] for _ in range(N + 1)]  # 1-based индексация
    in_degree = [0] * (N + 1)

    for _ in range(M):
        a = int(data[idx])
        idx += 1
        b = int(data[idx])
        idx += 1
        adj[a].append(b)
        in_degree[b] += 1

    # Инициализация очереди для вершин с нулевой степенью входа
    queue = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(topo_order) != N:
        print(-1)  # Граф содержит цикл, сортировка невозможна
    else:
        print(' '.join(map(str, topo_order)))


if __name__ == "__main__":
    main()