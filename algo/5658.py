import sys
sys.stdin = open('5658.txt', 'r')
#10시 58분 시작

for test in range(1, int(input())+1):
    N,K = map(int, input().split())
    arr = input()
    n = V = N//4
    re = set()
    for r in range(n):
        vertex = V-r
        for i in range(vertex,vertex+N,n):
            i = i % N
            num =''
            for j in range(n):
                jj = (i+j) % N
                num += arr[jj]
            else:
                num = '0x' + num
                num = int(num, 16)
                re.add(num)
    re = list(re)
    re.sort(reverse=True)
    print('#{} {}'.format(test, re[K-1]))