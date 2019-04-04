import sys
sys.stdin = open('electricbus_1v.txt', 'r') # 파일에서 읽을 때 사용

T = int(input())
for test_case in range (1, T + 1):
    K, N, M = map(int, input().split())
    print(K,N,M)
    arr = list(map(int, input().split()))
    print(arr)
    arr.append(N)
    arr.insert(0,0)
    ans = pos = 0
    for i in range(1, len(arr)):
       if arr[i]-arr[i-1] > K:
           ans = 0
           break
       else:
           if arr[i]> pos + K:
               pos = arr[i-1]
               ans += 1
    print(f'#{test_case} {ans}')