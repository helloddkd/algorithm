import sys
sys.stdin = open('5644.txt', 'r')


for test in range(1, int(input())+1):
    M,A = map(int, input().split())
    amove = [0] + list(map(int, input().split())) #초기상태 추가
    bmove = [0] + list(map(int, input().split()))
    BC = []
    for _ in range(A):
        x,y,C,P = map(int, input().split())
        BC.append([y-1, x-1, C,P])
    dr = [0,-1,0,1,0]
    dc = [0,0,1,0,-1]
    ar,ac = 0,0
    br,bc = 9,9
    totalcharge  = 0
    for t in range(M+1): #총 M초가 흐르는 동안 매초 상태
        ar += dr[amove[t]]
        ac += dc[amove[t]]
        br += dr[bmove[t]]
        bc += dc[bmove[t]]
        Ac,Bc = [], []

        for index, batterycharge in enumerate(BC):
            bcr, bcc, c, p = batterycharge
            if abs(ar-bcr) + abs(ac-bcc) <= c:
                Ac.append([p, index])
            if abs(bcr-br) + abs(bcc-bc) <= c:
                Bc.append([p, index])

        Ac.sort(reverse = True)
        Bc.sort(reverse = True)
        if Ac and Bc:
            if Ac[0][1] == Bc[0][1]:
                if len(Ac) == 1 and len(Bc) == 1:
                    totalcharge += Ac[0][0]
                elif len(Ac) > 1 and len(Bc) == 1:
                    totalcharge += Ac[1][0] + Bc[0][0]
                elif len(Ac) == 1 and len(Bc) > 1:
                    totalcharge += Ac[0][0] + Bc[1][0]
                else: #둘 다 1이상인데 최대가 같음
                    if Ac[1][0] >= Bc[1][0]:
                        totalcharge += Bc[0][0] + Ac[1][0]
                    else:
                        totalcharge += Ac[0][0] + Bc[1][0]
            else:
                totalcharge += Ac[0][0] + Bc[0][0]
        elif Ac: #Bc는 없음
            totalcharge += Ac[0][0]
        elif Bc:
            totalcharge += Bc[0][0]


    print('#{} {}'.format(test, totalcharge))











