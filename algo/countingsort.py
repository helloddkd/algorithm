A = [0,4,1,3,1,2,4,1]
Max = max(A)+1
Count = [0] * Max
temp = [0] * len(A)

print(A)
for i in range(len(A)):
    Count[A[i]] += 1
print(Count)
for j in range(1, len(Count)):
    Count[j] += Count[j-1]
print(Count)
for k in range(len(A)-1, -1, -1):
    Count[A[k]] -= 1
    temp[Count[A[k]]] = A[k]
print(temp)
