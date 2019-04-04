import sys
sys.stdin = open('2117.txt', 'r')

T = int(input())
for test in range(1,T+1):
    N,M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    if N % 2:
        K = N
    else:
        K = N+1
    Max = 0

    for r in range(N):
        for c in range(N):
            for k in range(K, 0, -1):
                S = 0
                for rr in range(r-k+1, r+k):
                    for cc in range(c-k+1, c+k):
                        if abs(rr-r) + abs(cc-c) < k and 0<=rr<N and 0<=cc<N and arr[rr][cc] > 0:
                            S += 1
                if S*M >= k*k + (k-1)*(k-1):
                    Max = max(Max, S)
    print('#{} {}'.format(test, Max))


#실행시간을 더 줄이고 싶으면 dfs로 해야 함. 모든 칸을 다 보는 게 아니라, home 리스트 안에 잇는 애들만 봐야 함.







