import sys
sys.stdin = open('mountain.txt', 'r')

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    maps = []
    for n in range(N):
        row = list(map(int, input().split()))
        maps += [row]
    X = [0, 0, 1, -1]
    Y = [1, -1, 0, 0]
    M = 0
    def findmap(point, h, rk, k=K, n=1, vis=[]):
        global M
        M = max(M, n)
        viss = vis + [point]
        for i in range(4):
            y = Y[i] + point[0]
            x = X[i] + point[1]
            if 0 <= y < N and 0 <= x < N and [y, x] not in viss:
                m = maps[y][x]
                if maps[y][x] < h:
                    findmap([y, x], m, rk, k, n + 1, viss)
                elif rk:
                    for r in range(1, k+1):
                        if 0 <= m - r and m - r == h - 1:
                            findmap([y, x], m-r, 0, k, n+1, viss)
    Mh = 0
    Ml = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] > Mh:
                Mh = maps[i][j]
                Ml = [[i, j]]
            elif maps[i][j] == Mh:
                Ml.append([i, j])
    for m in Ml:
        findmap(m, Mh, 1)
    print('#{} {}'.format(t+1, M))