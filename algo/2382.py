import sys
sys.stdin = open('2382.txt', 'r')


dirchange = {0:0, 1:2, 2:1, 3:4, 4:3}
for test in range(1, int(input())+1):
    N,M,K = map(int ,input().split())
    arr =[]
    for _ in range(K):
        arr.append(list(map(int, input().split())))
    dr = [0,-1,1,0,0]
    dc = [0,0,0,-1,1]
    while M>0:
        collide = []
        for index, cluster in enumerate(arr):
            r,c,num,dir = cluster
            if r != -1:
                rr = r+ dr[dir]
                cc = c + dc[dir]
                if rr == N-1 or rr == 0 or cc==N-1 or cc==0: #약품지대에 도착
                    arr[index] = [rr,cc, num // 2, dirchange[dir]]
                else:
                    arr[index][0], arr[index][1] = rr,cc
                for coll in collide:
                    if coll[0] == rr and coll[1] == cc:
                        coll.append(index)
                        break
                else:
                    collide.append([rr, cc, index])

        for col in collide:
            if len(col) > 3:
                Max = Sum = newdir = 0
                Maxindex = col[2]
                for i in range(2,len(col)):
                    Sum += arr[col[i]][2]
                    if arr[col[i]][2] > Max:
                        Max= arr[col[i]][2]
                        Maxindex = col[i]
                        newdir = arr[col[i]][3]
                    arr[col[i]] = [-1,-1,0,0]
                else:
                    arr[Maxindex] = [col[0],col[1], Sum, newdir]

        M-=1
    re = 0
    for k in range(len(arr)):
        re += arr[k][2]
    print('#{} {}'.format(test, re))