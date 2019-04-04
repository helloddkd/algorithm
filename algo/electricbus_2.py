import sys
sys.stdin = open('electricbus.txt', 'r')

T= int(input())
for test in range(T):
    stations = list(map(int, input().split()))
    dis = stations[0]-stations[1]
    print(dis)
    stations_change = stations[2:]
    print(stations)
    n = len(stations)
    stations = [x for x in range(n)]
    result = []
    for i in range(1 << n):
        sec = []
        for j in range(n - 1, -1, -1):
            if i & (1 << j):
                sec.append(stations[j])
        if sum(sec) == dis:
            result.append(sec)
    print(result)
    re = [len(x) for x in result]
    r = min(re)
    print(f'#{test+1} {r+1}')


