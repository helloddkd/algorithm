t = 'talkdjflsjaejfa;eijflappeldsfaljefajeflapplesdfss'
p = 'apple'

def boring(t,p):
    tl = len(t)
    pl = len(p)
    i=j=0
    while j < pl and i < tl:
        if t[i] != p[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == pl :
        return i-pl
    else:
        return -1
print(boring(t,p))



def recursive_boring(t,p,i=0,j=0):
    tl = len(t)
    pl = len(p)
    if j == len(p):
        return j-pl
    else:
        if t[i] != p[j]:
            i = i-j
            j = -1
        recursive_boring(t, p, i + 1, j + 1)

print(recursive_boring(t,p))