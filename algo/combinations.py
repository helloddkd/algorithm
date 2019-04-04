arr = [1, 2, 3, 4]

result = []
for n in range(1 << len(arr)): # range == 0 ~ 2^len(arr)-1 == 0 ~ 15
    # 모든 경우의 수는 2^len(arr)개 이다.
    answer = []  # answer 에 각 경우의 수를 포함시킨다.
    for i in range(len(arr)): # 해당 수와 2^i승이 이진법에서 일치하는지 확인한다.
        if n & (1<<i):
            answer.append(arr[i]) # 일치하는 부분이 있으면 append한다.
            if len(answer) == 2 and answer not in result:
                result.append(answer)
                print(answer)
                break

