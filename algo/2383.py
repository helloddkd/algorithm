import sys
sys.stdin = open('2383.txt', 'r')


from itertools import combinations
from collections import deque
for test in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    S = []
    P = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                P.append([r,c])
            elif arr[r][c] > 1:
                S.append([r,c, arr[r][c]])
    p = len(P)
    hi = [x for x in range(p)]
    Min = 9999
    for i in range(p+1):
        for com in list(combinations(hi, i)):
            S1 = []
            S2 = []
            for person in range(p):
                if person not in com:
                    S2.append([abs(S[1][0]-P[person][0]) + abs(S[1][1]-P[person][1]), person])
                else:
                    S1.append([abs(S[0][0]-P[person][0]) + abs(S[0][1]-P[person][1]), person])
            S2.sort()
            S1.sort()
            #s1과 s2로 가는 사람들 다 정해짐
            ons1 = []
            ons2 = []
            smin = min(S1[0][0] if S1 else 999, S2[0][0] if S2 else 999)
            if S1 and smin == S1[0][0]:
                while S1 and S1[0][0] == smin and len(ons1)<3:
                    ons1.append([S[0][2], S1.pop(0)])
            if S2 and smin == S2[0][0]:
                while S2 and S2[0][0] == smin and len(ons2)<3:
                    ons2.append([S[1][2], S2.pop(0)])
            t = smin+1
            while ons1 or ons2 or S1 or S2:
                index= 0
                while index < len(ons1):
                    if ons1[index][0] == 0:
                        ons1.pop(index)
                    else:
                        ons1[index][0] -= 1
                        index += 1
                ind = 0
                while ind < len(ons2):
                    if ons2[ind][0] == 0:
                        ons2.pop(ind)
                    else:
                        ons2[ind][0] -= 1
                        ind += 1
                if S1:
                    while S1[0][0]-t <= 0:
                        if len(ons1)<3:
                            if S1[0][0]-t == 0:
                                ons1.append([S[0][2], S1.pop(0)])
                            else:
                                ons1.append([S[0][2]-1, S1.pop(0)])
                            if len(ons1) == 3 or not S1:
                                 break
                        else:
                            break
                if S2:
                    while S2[0][0]-t <= 0:
                        if len(ons2)<3:
                            if S2[0][0]-t == 0:
                                ons2.append([S[1][2], S2.pop(0)])
                            else:
                                ons2.append([S[1][2]-1, S2.pop(0)])
                            if len(ons2) == 3 or not S2:
                                break
                        else:
                            break
                t += 1
            Min = min(Min, t-1)
    print('#{} {}'.format(test, Min))













