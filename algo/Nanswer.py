a = 0
for i in range(0,98):
    x = 1+i
    for j in range(i, 98):
        a+=1
        y = 1+j-i
        z = 100-x-y
        print(a, x,y,z)