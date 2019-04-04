import sys
sys.stdin = open('5653.txt', 'r')

for test in range(1, int(input())+1):
    N,M,K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    for y in range(N):
        for x in range(M):
            if arr[y][x] > 0:
                m = arr[y][x]
                arr[y][x] = [m,m,m]


    while len(arr[0]) < M+K:
        for i in range(N):
            arr[i].insert(0,0)
            arr[i].append(0)
    while len(arr)<N+K:
        arr.insert(0,[0]*len(arr[0]))
        arr.append([0]*len(arr[0]))
    N += K
    M += K

    #초기화완료, 이제 시간 흐르기 시작
    dr = [-1,1,0,0]
    dc = [0,0,1,-1]
    t = 0
    while t < K:
        t += 1
        visit = [[False]*M for __ in range(N)]
        for r in range(N):
            for c in range(M):
                if arr[r][c] != 0 and not visit[r][c]: #세포가 잇다
                    if arr[r][c][0] != 0: #비활성 상태
                        arr[r][c][0] -= 1
                    else: #활성상태일 가능성
                        if arr[r][c][1] > 0:
                            arr[r][c][1] -= 1
                            for i in range(4):
                                rr = r+dr[i]
                                cc = c+dc[i]
                                if 0<=rr<N and 0<=cc<M:
                                    if not arr[rr][cc]:
                                        arr[rr][cc] = [arr[r][c][2],arr[r][c][2],arr[r][c][2]]
                                        visit[rr][cc] = True
                                    elif arr[rr][cc] and visit[rr][cc]: #이번에 갓태어난해
                                        if arr[rr][cc][2] < arr[r][c][2]:
                                            arr[rr][cc] = [arr[r][c][2], arr[r][c][2], arr[r][c][2]]
                                            visit[rr][cc] = True
    cnt = 0
    for rrr in range(N):
        for ccc in range(M):
            if arr[rrr][ccc]!= 0 and (arr[rrr][ccc][0]>0 or arr[rrr][ccc][1]>0):
                cnt += 1
    print('#{} {}'.format(test, cnt))




