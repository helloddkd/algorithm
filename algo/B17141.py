import sys
sys.stdin = open('B17141.txt', 'r')


from itertools import combinations
def check(arr):
    for r in range(N):
        for c in range(N):
            if arr[r][c] in (0,2):
                return False
    else:
        return True

def bfs(virus, arr):
    global re
    while virus:
        r, c = virus.pop(0)
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < N and arr[rr][cc] in (0, 2):#벽이 아니면
                virus.append([rr,cc])
                arr[rr][cc] = arr[r][c]-1
                Min = arr[rr][cc]
                if (-Min)-1 >= re:
                    return
    if check(arr):
        re = (-Min)-1
        return
    return


dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
V = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 2:
            V.append([r, c])
re = N**2
whereto = list(combinations(V, M))
for virus in whereto:
    new_arr = [arr[y][:] for y in range(N)]
    for r,c in virus:
        new_arr[r][c] = -1
    else:
        bfs(list(virus), new_arr)
        pass
if re == N**2:
    print(-1)
else:
    print(re)

