import sys
sys.stdin = open("in1.txt", "rt")
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
"""
for i in range(len(a)):
    a[i].insert(0,0)
    a[i].append(0)
a.insert(0,([0]*(n+2)))
a.append(([0]*(n+2)))
cnt=0
for i in range(1,n+1):
    for j in range(1,n+1):
        now=a[i][j]
        if now>(a[i][j-1]) and now>a[i][j+1] and now>a[i-1][j] and now>a[i+1][j]:
            cnt+=1
print(cnt)
"""


a.insert(0,[0]*n)
a.append([0]*n)
for x in a:
    x.insert(0,0)
    x.append(0)
cnt=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)): 
            cnt+=1
print(cnt)
