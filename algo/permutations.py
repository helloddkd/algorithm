
arr = [1, 2, 3, 4]

# def searching(arrr, n=[], answer=[]):
#     # arrr: 순열을 찾으려는 리스트
#     # n : answer에 포함시킨 인덱스의 리스트
#     # answer : arrr의 순열들이 포함되는 리스트
#     if len(n) == 2:
#         print(answer) # arrr의 길이와 n에 해당하는 리스트의 길이가 같으면 print한다.
#     else:
#         for i in range(len(arrr)):
#             if i not in n:
#                 m = n + [i] # n이 for문 돌면서 초기화가 되지 않으므로 m이라는 새로운 리스트에 i를 포함시켜서 재귀를 돌림
#                 answers = answer + [arrr[i]] # answer가 for문이 돌면서 초기화가 되지 않으므로 answers라는 새로운 리스트에 arrr[i]를 포함시켜서 재귀를 돌림
#                 searching(arrr, m, answers)
# searching(arr)


def permutations(arr, k=-1 , index=[], answer=[]):
    if k == -1:
        k = len(arr)
    if len(index) == k:
        print(answer)
    else:
        for i in range(len(arr)):
            if i not in index:
                permutations(arr, k, index + [i], answer + [arr[i]])


permutations(arr,2)