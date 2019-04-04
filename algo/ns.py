import sys
sys.stdin = open('ns.txt', 'r')

for t in range(10):
    side = int(input())
    square = []
    S = []
    for _ in range(side):
        square.append(input().split())
 
    ans = 0
    for row in range(side):
        for col in range(side):
            if not S:
                if square[col][row] == "1":
                    S.append("1")
            elif square[col][row] == "2" and S[-1] == "1":
                S.append("2")
            elif square[col][row] == "1" and S[-1] == "2":
                S.append("1")
 
        while len(S) > 0:
            if "2" == S.pop():
                ans += 1
 
    print(f"#{t+1} {ans}")