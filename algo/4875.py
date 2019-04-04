import sys
sys.stdin = open('4875.txt', 'r')

T=int(input())
for test in range(1, T+1):
    N= int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, list(input()))))
    print(f'#{test} ', end="")


    st = arr[0].index(3)
    S = -1
    now = [0, st]
    Stack = [now + [S]]
    a = Stack[-1]
    while arr[now[0]][now[1]] != 2:
        if now[0]<N-1 and arr[now[0]+1][now[1]] in (0,2) and a[-1]!=2:
            now[0] += 1
            S=2
        elif now[1]<N-1 and arr[now[0]][now[1]+1] in (0,2) and S!= 0:
            now[1] += 1
            S=1
        elif now[1]>0 and arr[now[0]][now[1]-1] in (0,2) and S != 1:
            now[1] -= 1
            S=0
        else:
            if len(Stack) == 0:
                print(0)
                break
            else:
                a = Stack.pop()
                now = [a[0], a[1]]
                S = a[-1]
                continue
        Stack.append(now + [S])
    else:
        print(1)



