from queue import Queue


import sys
sys.stdin = open('5247_advance_4.txt', 'r')

T = int(input())
for test in range(1,T+1):
    N,M = list(map(int,input().split()))
    #M에서 매번 +1 -1 /2 +10 4가지 선택지가 나타난다. 브루트포스..?
    #BFS로 해야 하나? 응..
    #
    print(f'#{test} {count}')
