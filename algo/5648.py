import sys
sys.stdin = open('5648.txt', 'r')

from collections import deque()
for test in range(1, int(input())+1):
    N = int(input())
    L, R, U, D = deque(), deque(), deque(), deque()
    for _ in range(N):
        temp = list(map(int, input().split()))
        if temp[2] == 0:
            U.append(temp)
        elif temp[2] == 1:
            D.append(temp)
        elif temp[2] == 2:
            L.append(temp)
        else:
            R.append(temp)
    U.sort()
    D.sort()
    L.sort()
    R.sort()

    i = 0
    while L[0] < R[0]:
        L.popleft()
    while i < len(L) and i<len(R):
        total += L[i][2] + R[i][2]

    while



    total = 0
    while True:
        ch = 0
        E = []
        dis = 2001
        for i, l in enumerate(L):
            for j, r in enumerate(R):
                if l[1] == r[1] and 0< l[0]-r[0] < dis:
                    dis = l[0]-r[0]
                    E = [[i,j]]
                elif l[0]-r[0] == dis:
                    E.append([i,j])
        for e in E:
            total += L[i][3] + R[j][3]
            ch += 1
            del(L[i])
            del(R[j])
        dis = 2001
        EE=[]
        for a, u in enumerate(U):
            for b, d in enumerate(D):
                if u[0] == d[0] and 0<= d[1]-u[1] < dis:
                    dis = d[1]-u[1]
                    EE = [[a,b]]
                elif d[1]-u[1] == dis:
                    EE.append([a,b])
        for ee in EE:
            total += U[a][3] + D[b][3]
            ch +=1
            del(U[a])
            del(D[b])
        if ch == 0:
            break
    print('#{} {}'.format(test, total))

