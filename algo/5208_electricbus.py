import sys

sys.stdin = open('electricbus.txt', 'r')

T= int(input())
for test in range(T):
    stations = list(map(int, input().split()))
    N = int(stations[0])
    stations.append(N)
    print(stations)
    status, count = 1, -1
    k = stations[1]
    while status <= N-1:
        count += 1
        if k == 1:
            status += 1
            if status >= N:
                break
            k = stations[status]
        else:
            re = idx = 0
            if status + k <= N:
                for i in range(k):
                    if stations[status+k-i] > re:
                        if i != stations[status+k-i]:
                            re = stations[status+k-i]
                            idx = status + k - i
                status = idx
                k = stations[status]
            else:
                break
    print(f'#{test+1} {count}')
