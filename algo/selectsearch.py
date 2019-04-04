arr = [80,90,70,80,90,99,100,23,54,59,69]
#중간값을 찾는다고 해보자
if len(arr) %2 ==0:
    mid = len(arr)//2
else:
    mid = len(arr)//2 +1

def selectsearch(arr, k):
    for i in range(k):
        minI = i
        for j in range(i+1,len(arr)):
            if arr[minI]>arr[j]:
                minI = j
        arr[minI], arr[i] = arr[i], arr[minI]
    return arr[k-1]

print(selectsearch(arr, mid))
print(mid, len(arr))
print(sorted(arr))