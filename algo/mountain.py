import sys
sys.stdin = open('mountain.txt', 'r')


def bfs(y, x, h, path=[], d=1, S=1):
    global H
    H = max(d, H)
    pathh = path + [[y, x]]
    for i in range(4):
        r = y + dr[i]
        c = x + dc[i]
        if 0 <= r < N and 0 <= c < N and [r, c] not in path:
            if arr[r][c] < h:
                bfs(r,c,arr[r][c], pathh, d+1, S)
            elif S==1:
                    for k in range(1,K+1):
                        if 0 <= arr[r][c] - k and arr[r][c] - k == h - 1:
                            bfs(r,c,arr[r][c]-k, pathh, d+1, 0)


T = int(input())
for test in range(1,T+1):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    highest = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] > highest:
                highest = arr[r][c]
    H = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for rr in range(N):
        for cc in range(N):
            if arr[rr][cc] == highest:
                bfs(rr,cc, arr[rr][cc], [],1,1)

    print('#{} {}'.format(test,H))