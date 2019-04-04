Array = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(len(Array[0])):
	for j in range(len(Array)):
		print(Array[j][i])

print('====================================')
m = len(Array[0])

for i in range(len(Array)):
	for j in range(len(Array[0])):
		print(Array[i][j+(m-1-2*j) * (i%2)])

print('====================================')
m = len(Array[0])

for i in range(len(Array)):
    for j in range(len(Array[0])):
        if i%2==1:
            print(Array[i][m-1-j])
        else:
            print(Array[i][j])

print('===============')
for i in range(len(Array)):
    for j in range(len(Array[0])):
        if i < j:
            Array[i][j], Array[j][i] = Array[j][i], Array[i][j]
print(Array)