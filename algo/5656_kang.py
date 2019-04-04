dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def brock(n, x, y):
    global W, H
    a = data[n][x][y]
    data[n][x][y] = 0
    for i in range(1, a):
        for j in range(4):
            nx, ny = x + (i * dx[j]), y + (i * dy[j])
            if 0 <= nx < H and 0 <= ny < W and data[n][nx][ny]:
                brock(n, nx, ny)


def clear(n):
    global W, H
    for i in range(W):
        for j in range(H - 1, -1, -1):
            if data[n][j][i] == 0:
                for k in range(j - 1, -1, -1):
                    if data[n][k][i] != 0:
                        data[n][j][i], data[n][k][i] = data[n][k][i], data[n][j][i]
                        break


def shoot(n, shot):
    global H
    for i in range(H):
        if data[n][i][shot] == 0:
            continue
        else:
            brock(n, i, shot)
            break
    clear(n)


def cnt(n):
    global W, H
    brick = 0
    for i in range(W):
        for j in range(H):
            if data[n][j][i] != 0:
                brick += 1
    return brick


def sol(n):
    global N, W, H, ans
    if n == N + 1:
        a = cnt(n - 1)
        if a < ans:
            ans = a
        return
    for shot in range(W):
        for i in range(H):
            for j in range(W):
                data[n][i][j] = data[n - 1][i][j]
        shoot(n, shot)
        sol(n + 1)


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    data = [[list(map(int, input().split())) for _ in range(H)]]
    for _ in range(4):
        data.append([[0] * W for _ in range(H)])
    ans = 1 << 30
    sol(1)
    print('#{} {}'.format(tc, ans))