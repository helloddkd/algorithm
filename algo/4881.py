import sys
sys.stdin = open('4881.txt', 'r')

T=int(input())
for test in range(1,T+1):
    N=int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    print(arr)
    Min = 0
    for i in range(N):
        Min += arr[i][i]

    i = 0
    Stack = []
    re = 0

    while i < N:
        for c in range(N):
            for r in range(N):
                if c not in Stack:
                    re += arr[r][c]
                    Stack.append((r, c))





# 대각합을 하나 구해서 Min으로 잡는다
# 첫 시작 0행 n경우의수, 그리고 1행의 N-1경우의수 2행의 N-2경우의 수 n-1행의 1경우의 수
# list에 인덱스값을 담고, 한 단계 내려갈때마다 지우기.
# 한 단계 끝날때마다 Min과 비교해서 아니면 바로 나가기