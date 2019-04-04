dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def isarr(r, c):
    return True if 0 <= r < H and 0 <= c < W else False


def BFS(r, c, arr):
    d = arr[r][c]
    arr[r][c] = 0
    if d > 1:
        for i in range(4):
            for j in range(1, d):
                ny = r + dy[i] * j
                nx = c + dx[i] * j
                if isarr(ny, nx) and arr[ny][nx]:
                    BFS(ny, nx, arr)


def count(arr):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                cnt += 1
    return cnt


def where(cnt, dep, arr):
    global res
    arr_ = [[0] * W for i in range(H)]
    for i in range(H):
        for j in range(W):
            arr_[i][j] = arr[i][j]
    h = -1
    for i in range(H):
        if arr[i][cnt]:
            h = i
            break
    if h == -1:
        res = min(res, count(arr_))
        return
    BFS(h, cnt, arr_)

    for i in range(W):
        z_idx = flag = 0
        for j in range(H):
            if not arr_[H - j - 1][i] and not flag:
                z_idx = H - j - 1
                flag = 1
            if arr_[H - j - 1][i] and flag:
                arr_[z_idx][i] = arr_[H - j - 1][i]
                arr_[H - j - 1][i] = 0
                z_idx -= 1

    if dep == N - 1:
        res = min(res, count(arr_))
        return
    for i in range(W):
        where(i, dep + 1, arr_)


T = int(input())
for _ in range(T):

    res = 180
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(H)]

    for i in range(W):
        where(i, 0, arr)
    print(f"#{_ + 1} {res}")