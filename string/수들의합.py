import sys

# n=8
# m=3
# a=[1,2,1,3,1,1,1,2]
# n=10
# m=5
# a=[3,2,2,1,3,1,2,3,2,2]
n,m=map(int,input().split())
a=list(map(int,input().split()))
lt=0
rt=1
cnt=0
# tot=0
# while True:
#     if a[lt]==m:
#         cnt+=1
#         lt+=1
#         rt=lt+1
#         tot=0
#         continue
#     if rt==len(a):
#         break
#     tot+=(a[lt]+a[rt])
#     if tot==m:
#         cnt+=1
#         lt+=1
#         rt=lt+1
#         tot=0
#     elif tot>m:
#         lt+=1
#         rt=lt+1
#         tot=0
#     elif tot<m:
#         tot-=a[lt]
#         rt+=1
# tot=[]
# while rt<=len(a):
#     if a[lt]==m:
#         cnt+=1
#         lt+=1
#         rt=lt+1
#         tot=[]
#         continue
#     tot=a[lt:rt]
#     stot=sum(tot)
#     if stot==m:
#         cnt+=1
#         lt+=1
#         rt=lt+1
#         tot=[]
#     elif stot>m:
#         lt+=1
#         rt=lt+1
#         tot=[]
#     else:
#         rt+=1
#         tot=[]
tot=a[0]
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else: #rt==n
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1

print(cnt)