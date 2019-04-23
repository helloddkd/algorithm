import sys
sys.stdin = open('B17143.txt', 'r')


def move(t):
    global arr, Sum
    samecol = []
    for j in range(len(arr)):
        if arr[j][1] == t: #낚시꾼과 같은 열
            samecol.append(arr[j])
    if samecol:
        samecol.sort()
        Sum += samecol[0][4]
        arr.remove(samecol[0])

    for i in range(len(arr)):
        r,c, V, d = arr[i][0], arr[i][1], arr[i][2], arr[i][3]
        v = V
        if d == 1 and r == 1: d = 2
        elif d == 2 and r == R: d = 1
        elif d == 3 and c == C: d=4
        elif d ==4 and c == 1: d=3

        while v>0 and d in (1,2):
            v -= 1
            if d == 1:
                r -= 1
                if r <= 1:
                    d = 2
            else:
                r += 1
                if r >= R:
                    d = 1
        while v>0 and d in (3, 4):
            v -= 1
            if d == 3:
                c += 1
                if c >= C:
                    d = 4
            else:
                c -= 1
                if c <= 1:
                    d = 3
        arr[i] = [r,c,V,d, arr[i][4]]
    poplist = set()
    for s in range(len(arr)-1,0,-1):
        for o in range(s-1,-1,-1):
            if arr[s][0] == arr[o][0] and arr[s][1] == arr[o][1]:
                if arr[s][4] > arr[o][4]:
                    poplist.add(o)
                else:
                    poplist.add(s)
    poplist = list(poplist)
    poplist.sort(reverse=True)
    for ind in poplist:
        arr.pop(ind)


R, C, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
Sum = 0
if M == 0:
    print(0)
else:
    for t in range(1, C+1):
        move(t)
    print(Sum)