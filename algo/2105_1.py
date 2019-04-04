import sys
sys.stdin = open('2105.txt', 'r')

nod = {0:3, 1:2, 2:1, 3:0, -1:-1}

def DFS(r,c,str,stc,path=[], d=-1,dirpath=[-1]):
    global cnt
    if d == -1:
        if arr[r-1][c+1] != path[0]:
            DFS(r-1,c+1,str,stc,path+[arr[r-1][c+1]], 0, [0])
    else:
        for i in range(4):
            if i != nod[d]:
                rr = r+dr[i]
                cc = c+dc[i]
                if 0<=rr<N and 0<=cc<N:
                    if i not in dirpath or i == dirpath[-1]:
                        if arr[rr][cc] not in path:
                            DFS(rr,cc,str,stc,path+[arr[rr][cc]],i, dirpath+[i] if i!=dirpath[-1] else dirpath)
                        elif rr==str and cc==stc:
                            cnt +=1
                            print(str,stc,dirpath)
                            return


dr = [-1,-1,1,1]
dc = [1,-1,1,-1]
for test in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #N-3+1이 최대길이
    cnt = 0
    for r in range(1,N-1):
        for c in range(N-2):
            DFS(2,1,2,1,[arr[2][1]])
    print(cnt)