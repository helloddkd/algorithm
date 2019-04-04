import sys
sys.stdin = open('B8979.txt', 'r')

N, K = map(int, input().split())
nations = []
for n in range(N):
    nation = list(map(int, input().split()))
    nations += [nation]

def qsort(na, m):
    if len(na) <= 1:
        return na
    pivot = na[len(na) >> 1][m]
    L = []
    R = []
    E = []
    for a in na:
        if a[m] < pivot:
            R.append(a)
        elif a[m] > pivot:
            L.append(a)
        else:
            E.append(a)
    if m <= 2:
        E = qsort(E, m+1)
    return qsort(L, m) + E + qsort(R, m)

nations = qsort(nations, 1)
answer = 0
for i in range(len(nations)):
    if nations[i][0] == K:
        q = 1
        while i - q >= 0:
            if nations[i][1:] == nations[i-q][1:]:
                q += 1
            else: break
        answer = i - q + 2
        break
print(answer)
