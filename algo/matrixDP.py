import sys
sys.stdin = open('matrixDP.txt', 'r')

def makemat(mat = [], index=[]):
    if len(mat) == N:
        return mat
    for j in range(N):
        if j not in index and a[j] == mat[-1][1]:
            mat.append([a[j], b[j]])
            return makemat(mat, index+[j])


T= int(input())
for test in range(1, T+1):
    N = int(input())
    a = []
    b = []
    can = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        a.append(temp[0])
        b.append(temp[1])
    Min = max(max(a),max(b))**max(max(a),max(b))
    for i in range(N):
        M = makemat([[a[i], b[i]]], [i])
        if M:
            print(M)
            S = 0
            for k in range(N-1):
                re = [M[0][0], M[k+1][1]]
                S+= re[0] * M[k][1] * re[1]
            Min = min(Min, S)
    print(Min)
    print()