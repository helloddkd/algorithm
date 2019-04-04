import sys
sys.stdin = open('5656.txt', 'r')

from copy import deepcopy
def collide(r,c, arr, blocks):
    b = arr[r][c]
    L = R = U = D = 1
    while L < b and c-L>=0:
        if arr[r][c - L] != 0:
            collide(r, c+L, arr, blocks)
            arr[r][c+L] = 0
            blocks -= 1
        L += 1

    while R < b and c+R<W:
        if arr[r][c + R] != 0:
            collide(r, c+R, arr, blocks)
            arr[r][c+R] = 0
            blocks -= 1
        R += 1

    while U < b:
        if arr[r-U][c] != 0:
            collide(r-U, c, arr, blocks)
            arr[r-U][c] = 0
            blocks -= 1
        R += 1
    while D < b:
        if arr[r+D][c] != 0:
            collide(r+D, c, arr, blocks)
            arr[r+D][c] = 0
            blocks -= 1
        D += 1
    arr[r][c] = 0
    blocks -= 1
    return blocks

def drop(n, arr, blocks, per = []):
    global Min
    see = Min
    copy = deepcopy(arr)
    B = blocks
    perr = per + [n]
    for r in range(H):
        if arr[r][n] != 0:
            B = collide(r,n, copy, B)
            break
    if len(perr) == N:
        Min = min(Min, B)
        return
    for k in range(W-1,-1,-1):
        drop(k, copy, B, perr)



T = int(input())
for test in range(1, T+1):
    N,W,H = map(int, input().split())
    Map = []
    Blocks = Min = W*H
    for _ in range(H):
        temp = list(map(int,input().split()))
        Map.append(temp)
        Blocks -= temp.count(0)
    # for i in range(W):
    arr = deepcopy(Map)
    blocks = Blocks
    drop(9, arr, blocks)
    print(Min)