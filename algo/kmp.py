p = 'abcdacbef'                                                                       # pattern
t = 'alksdabcdabcflaskjflkabcdjsaflkjasdkdsajfabcdabceflksadjabcdaksfjffsdaf'      # text


m, n = len(p), len(t)
next = [-1] * m
temp = ''

for i in range(len(p)-1):
    for j in range(i+1, len(p)):
        if p[i] == p[j]:
            next[j] = i
print(next)
#
# # 전처리
# next[0] = -1
# i, j = 0, -1
# while i < m:
#     while j >= 0 and p[j] != p[i]:
#         j = next[j]
#     i, j = i + 1, j + 1
#     next[i] = j
#
# print(next)
#
# # 매칭
# i = j = 0
# while i < n:
#     while j >= 0 and p[j] != t[i]:
#         j = next[j]
#
#     i, j = i + 1, j + 1
#
#     if j == m:
#         print(i - j, t[i - j:])
#         break
