import sys
sys.stdin=open('0228.txt', 'r')

T=int(input())
for test in range(1,T+1):
    P, Q, R, S, W = list(map(int, input().split()))

    ansa = W*P
    if W <= R:
        ansb = Q
    else:
        ansb = Q +(W-R)*S

    print(f'#{test} {min(ansa,ansb)}')