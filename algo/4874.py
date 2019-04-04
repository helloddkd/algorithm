import sys
sys.stdin = open('4874.txt', 'r')

T = int(input())
for test in range(1, T+1):
    arr = input().split()
    S = []
    what = ['+', '-', '/', '*']
    print(f'#{test} ', end="")
    r = 1
    for ar in arr:
        try:
            S.append(int(ar))
        except:
            if ar == '.':
                print(S[-1])
            else:
                if len(S) > 1:
                    k =  what.index(ar)
                    if k == 0:
                        s = S.pop(-2) + S.pop(-1)
                    elif k == 1:
                        s = S.pop(-2) - S.pop(-1)
                    elif k == 2:
                        if S[-1] != 0:
                            s = S.pop(-2) // S.pop(-1)
                        else:
                            r = 0
                            break
                    elif k == 3:
                        s = S.pop(-2) * S.pop(-1)
                    S.append(s)
                else:
                    r=0
                    break
    if r== 0:
        print('error')

