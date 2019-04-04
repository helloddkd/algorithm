import sys
sys.stdin = open('2383.txt', 'r')
T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    queue = []
    e = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                queue.append([i, j])
            if arr[i][j] > 1:
                e.append([i, j, arr[i][j]])
    D = []

    for person in queue:
        a = []
        for stair in e:
            dis = abs(stair[0] - person[0]) + abs(stair[1] - person[1]) + 1
            a.append(dis + stair[2])
        D.append(a)

    res = []
    r1 = 0
    r2 = 0
    m = 0
    m_i = 0
    for i in D:
        if i[0] < i[1]:
            r1 += 1
            res.append([i[0], 1, m_i])
            if m > i[0]:
                m = i[0]
        else:
            r2 += 1
            res.append([i[1], 2, m_i])
            if m > i[1]:
                m = i[1]
        m_i += 1
    res.sort()
    for i in res:
        if r1 > 3:
            i[0] = min(i[0] + e[0][2], D[i[2]][1])
            r1 -= 1
        if r2 > 3:
            i[0] = min(i[0] + e[1][2], D[i[2]][0])
            r2 -= 1
    r = 0
    for i in res:
        r = max(i[0], r)
    print(f"#{_ + 1} {r}")