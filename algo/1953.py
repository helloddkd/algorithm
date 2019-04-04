import sys #10시 17분 시작
sys.stdin = open('1953.txt' ,'r')


tunnel = {
    1:[[-1,1,0,0], [0,0,-1,1], [1,2,5,6],[1,2,4,7],[1,3,4,5],[1,3,6,7]],
    2:[[-1,1,0,0],[0,0,0,0], [1,2,5,6],[1,2,4,7],[],[]],
    3:[[0,0,0,0],[0,0,-1,1],[],[],[1,3,4,5],[1,3,6,7]],
    4:[[-1,0,0,0],[0,0,0,1], [1,2,5,6],[],[],[1,3,6,7]],
    5:[[0,1,0,0],[0,0,0,1], [],[1,2,4,7],[],[1,3,6,7]],
    6:[[0,1,0,0],[0,0,-1,0],[],[1,2,4,7],[1,3,4,5],[]],
    7:[[-1,0,0,0],[0,0,-1,0],[1,2,5,6],[],[1,3,4,5],[]]
}
from collections import deque
for test in range(1,int(input())+1):
    N,M,R,C,L = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    Q = deque()
    Q.append([R,C])
    visited = [[False]*M for __ in range(N)]
    visited[R][C] = 1
    cnt = 1
    while Q:
        r,c = Q.popleft()
        if visited[r][c] == L:
            break
        Dir = tunnel[arr[r][c]]
        for i in range(4):
            rr = r+Dir[0][i]
            cc = c+Dir[1][i]
            if 0<=rr<N and 0<=cc<M and not visited[rr][cc] and arr[rr][cc] in Dir[2+i]:
                Q.append([rr,cc])
                visited[rr][cc] = visited[r][c] + 1
                cnt += 1
    print('#{} {}'.format(test, cnt))







