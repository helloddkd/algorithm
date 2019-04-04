import sys
sys.stdin = open('2105.txt', 'r')

def DFS(r,c, val, str, stc, d=-1, cnt=0, path=[], visit=[], dirpath=[]):
    global Max
    if dirpath:
        for kk in range(len(dirpath)-1):
            if dirpath[kk] == 0:
                if dirpath[kk+1] != 2:
                    return
            elif dirpath[kk] == 1:
                if dirpath[kk+1] != 0:
                    return
            elif dirpath[kk] == 2:
                if dirpath[kk+1] != 3:
                    return
            else:
                if dirpath[kk+1] != 1:
                    return
    pathh = path + [val]
    visitt = visit + [[r,c]]
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0<=rr<N and 0<=cc<N:
            if [rr,cc] not in visitt:
                if arr[rr][cc] not in pathh and cnt<=4:
                    DFS(rr,cc, arr[rr][cc], str,stc,i,cnt+1 if d!=i else cnt,pathh, visitt, dirpath+[i] if d!=i else dirpath)
            elif rr == str and cc == stc and len(pathh)>2 and cnt in (3,4):
                Max=max(Max, len(pathh))
                return

for test in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1,-1,1,1]
    dc = [1,-1,1,-1]
    Max = 0
    for r in range(1,N-1):
        for c in range(1,N-1):
            DFS(r,c, arr[r][c], r,c)
    print('#{} {}'.format(test, Max if Max>0 else -1))

