import sys
sys.stdin = open('1249.txt', 'r')

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for test in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dp = [[-1]*N for __ in range(N)]
    dp[0][0] = 0
    for c in range(N):
        for r in range(N):
            values=[]
            for i in range(4):
                rr = r+dr[i]
                cc = c+dc[i]
                if 0<=rr<N and 0<=cc<N and dp[rr][cc]!=-1:
                    values.append(dp[rr][cc])
            if values:
                dp[r][c] = min(values)+arr[r][c]
    print('#{} {}'.format(test, dp[-1][-1]))
