import sys
sys.stdin = open('1249.txt', 'r')



def dfs(r,c,visited,time=0):
    global Min
    if r == N-1 and c == N-1:
        Min = min(Min, time)
        return
    for i in range(4):
        rr = r+dr[i]
        cc = c+dc[i]
        if 0<=rr<N and 0<=cc<N and not visited[rr][cc] and time+arr[rr][cc]<Min:
            visited[rr][cc]=True
            dfs(rr,cc, visited, time+arr[rr][cc])
            visited[rr][cc]=False

def deq(S=[]):
    global Min
    see=Min
    visited = [[False]*N for _ in range(N)]
    visited[0][0]=1
    S.append([0,0,-1,0])
    while S:
        r, c, d, t = S.pop()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < N and i!=changedir[d] and t+arr[rr][cc] < Min:
                if rr == N-1 and cc==N-1:
                    Min = min(Min, t)
                else:
                    visited[rr][cc]=visited[r][c]+arr[rr][cc]
                    S.append([rr,cc,i,t+arr[rr][cc]])
from collections import deque
changedir={-1:-1, 0:1, 1:0, 2:3, 3:2}
dr = [0,0,1,-1]
dc = [1,-1,0,0]
for test in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    k=0
    for r in range(1,N):
        k += arr[r][-1]
    Min = sum(arr[0]) + k
    visited = [[False] * N for _ in range(N)]
    visited[0][0]=True
    # dfs(0,0, visited)
    deq()
    print('#{} {}'.format(test, Min))




    # if S>=Min:
    #     return
    # if r == N-1 and c == N-1:
    #     Min = min(Min, S)
    #     return
    # pathh = path+[[r,c]]
    # for i in range(4):
    #     rr = r+dr[i]
    #     cc = c+dc[i]
    #     if 0<=rr<N and 0<=cc<N and [rr,cc] not in pathh and S+arr[rr][cc]<Min:
    #         dfs(rr,cc, pathh, S+arr[rr][cc])



    # while S:
    #     r, c = S.pop()
    #     for i in range(4):
    #         rr = r + dr[i]
    #         cc = c + dc[i]
    #         if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc] and time+arr[rr][cc] < Min:
    #             if rr == N-1 and cc==N-1:
    #                 Min = min(Min, time)
    #             else:
    #                 S.append([rr,cc])
    #                 visited[rr][cc]=True
    #                 time += arr[rr][cc]