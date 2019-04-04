arr=[0,1,2,3,4,5,6,6,3,2,6,8,7,9]
arr = sorted(arr)
n = len(arr)
key = 10

print(arr)

def sequentialsearch(arr,n,key):
    for i in range(n):
        if arr[i] == key:
            return i
        else:
            continue
    else:
        return -1

print(sequentialsearch(arr,n,key))

arr=[0,1,2,3,4,5,6,6,3,2,6,8,7,9]
arr = sorted(arr) #오름차순정렬
n = len(arr)
key = 10

def sequentialsearch2(arr, n, key):
    for i in range(n):
        if arr[i] > key:
            return -1
        elif arr[i] == key:
            return i
        else:
            continue
    else:
        return -1

print(sequentialsearch2(arr,n,key))