import sys
sys.stdin = open("in1.txt", "rt")
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
#2차원리스트 읽기
# m=n//2
# apple=0
# for i in range(0,n):
#     if i<=m:
#         for j in range(m-i,(i+1)+m):
#             apple+=a[i][j]
#             # print(a[i][j])
#     else:
#         for k in range(i-m,n-i+m):
#             apple+=a[i][k]
#             # print(a[i][k])
# print(apple)

res=0
s=e=n//2
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)