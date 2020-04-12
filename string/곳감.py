import sys
sys.stdin = open("in1.txt", "rt")
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
#2차원리스트 읽기
"""
r=int(input())
for i in range(r):
    b=list(map(int,input().split()))
    rot_num=b[0]-1 #2
    rot_cnt=b[2] # 3
    tmp=[0]*n
    #print(tmp)
    for i in range(0,n):
        if b[1]==0:
            if i<rot_cnt: #3 01234 0이면 2로 5-3
                tmp[i+n-rot_cnt]=a[rot_num][i]
            else:
                tmp[i-rot_cnt]=a[rot_num][i]
        else:
            if i+rot_cnt>=n:
                tmp[i-n+rot_cnt]=a[rot_num][i]
            
            else:
                tmp[i+rot_cnt]=a[rot_num][i]
    #print(tmp)
    a[rot_num]=tmp
    #print(a)

# s=0 e=n
# s=1 e=n-1
# s=2 e=n-2
# s=1 e=n-1
# s=0 e=n
s=0
e=n
total=0
for i in range(n):
    for j in range(s,e):
        total+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(total)
"""



m=int(input())
for i in range(m):
    h,t,k=map(int,input().split())
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0,a[h-1].pop())
res=0
s=0
e=n-1
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)