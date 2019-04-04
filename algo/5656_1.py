import sys
sys.stdin = open('5656.txt', 'r')

from collections import deque
def collide(r,c, arr, blocks):
    b = arr[r][c] #몇개의 구슬을 연달아 삭제해야 하는지 값을 잡아둠
    arr[r][c] = 0 #먼저 부딪힌 지점의 구슬을 깨서 0으로 만들어줌
    blocks -= 1 #총 블럭 개수에서 1을 뺀다.

    L = R = U = D = 1 #4방으로 구슬에 쓰여진 개수-1만큼 깬다.
    while L < b and W>c-L>=0:
        if arr[r][c - L] != 0:
            arr, blocks = collide(r, c-L, arr, blocks) #만약 깨지는 범위 안에 다른 구슬이 또 있으면 그 구슬도 깨준다.
        L += 1
    while R < b and 0<=c+R<W:
        if arr[r][c + R] != 0:
            arr, blocks = collide(r, c+R, arr, blocks)
        R += 1
    while U < b and 0<=r-U<H:
        if arr[r-U][c] != 0:
            arr, blocks = collide(r-U, c, arr, blocks)
        U += 1
    while D < b and 0<=r+D<H:
        if arr[r+D][c] != 0:
            arr, blocks = collide(r+D, c, arr, blocks)
        D += 1
    return arr, blocks

def makepermu(n=0, per = []):
    global Min
    perr = per + [n]
    if len(perr) == N:
        arr = [Map[k][:] for k in range(H)]
        blocks = Blocks
        for i in range(N):
            for r in range(H):
                if arr[r][perr[i]] != 0:
                    arr, blocks = collide(r, perr[i], arr, blocks)
                    break
            #한번한번 터뜨리고 나서 0을 정리해줘야함
            no = []
            for rr in range(H-1,-1,-1): #맨밑에줄부터 본다
                if len(no) == W:
                    break
                for cc in range(W):
                    if arr[rr][cc] == 0 and cc not in no:
                        Q = deque()
                        for k in range(rr-1,-1,-1):
                            if arr[k][cc] != 0:
                                Q.append(arr[k][cc])
                                arr[k][cc] = 0
                        if len(Q): #0인데 그 위에 0아닌 것이 하나라도 있으면
                            jj = 0
                            while Q:
                                arr[rr-jj][cc] = Q.popleft()
                                jj += 1
                        else:
                            no.append(cc)
        Min = min(Min, blocks)
        return
    for j in range(W-1,-1,-1):
        makepermu(j, perr)

T = int(input())
for test in range(1, T + 1):
    N, W, H = map(int, input().split())
    Map = []
    Blocks = Min = W * H
    for _ in range(H):
        temp = list(map(int, input().split()))
        Map.append(temp)
        Blocks -= temp.count(0)
    Min = W*H
    for i in range(W-1,-1,-1):
        makepermu(i)
    print('#{} {}'.format(test, Min))