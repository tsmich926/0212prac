import sys
sys.stdin = open("jip.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N ,M = map(int,input().split())
    arr =[list(map(int,input().split())) for _ in range(N)]
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    lst = []
    for n in range(N):
        for m in range(M):
            sum = 0
            sum += arr[n][m]
            for k in range(4):
                new_r =n+dr[k]
                new_c = m+dc[k]
                if 0 <= new_r <N and  0<= new_c <M:
                    sum += arr[new_r][new_c]
        lst.append(sum)
    mmax = 0
    for j in range(len(lst)):
        if mmax < lst[j]:
            mmax = lst[j]
    print(f'#{tc} {mmax}')