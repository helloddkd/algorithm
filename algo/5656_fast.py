import sys
sys.stdin = open('5656.txt', 'r')

def dfs(t, pre_map):
    global my_min
    global n, w, h
    if pre_map.count(0) >= h * w:
        my_min = 0
        return
    if t >= n:
        result = h * w - pre_map.count(0)
        if result < my_min:
            my_min = result
        return
    for i in range(w):
        for j in range(h):
            if pre_map[i + w * j] > 0:
                temp2_map = pre_map[:]
                bomb(i + w * j, temp2_map)
                pull(temp2_map)
                dfs(t + 1, temp2_map)
                break


def bomb(k, pre_map):
    global w
    global h
    if pre_map[k]:
        if pre_map[k] == 1:
            pre_map[k] = 0
        else:
            t = pre_map[k] - 1
            pre_map[k] = 0
            for i in range(1, t + 1):
                if k % w + i < w:
                    bomb(k + i, pre_map)
                if k % w - i >= 0:
                    bomb(k - i, pre_map)
                if k + i * w < w * h:
                    bomb(k + i * w, pre_map)
                if k - i * w >= 0:
                    bomb(k - i * w, pre_map)


def pull(pre_map):
    global w
    global h
    for k in range(h - 1, -1, -1):
        for i in range(w):
            if pre_map[i + w * k] == 0:
                for t in range(k - 1, -1, -1):
                    if pre_map[i + w * t] > 0:
                        pre_map[i + w * k] = pre_map[i + w * t]
                        pre_map[i + w * t] = 0
                        break


for a in range(int(input())):
    n, w, h = list(map(int, input().split()))
    fst_map = []
    for i in range(h):
        fst_map.extend(list(map(int, input().split())))
    my_min = w*h
    dfs(0, fst_map)
    print('#{} {}'.format(a+1, my_min))