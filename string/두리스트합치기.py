import sys

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
# a=[1,3,5]
# b=[2,3,6,7,9]
c=[]
p1=0
p2=0
while len(c) != (len(a)+len(b)):
    if p1==len(a):
        c=c+b[p2:]
        break
    elif p2==len(b):
        c=c+a[p1:]
        break
    if a[p1]>=b[p2]:
        c.append(b[p2])
        p2+=1
    else:
        c.append(a[p1])
        p1+=1

# if p1<n:
#     c=c+a[p1:]
# if p2<m:
#     c=c+b[p2:]

for i in c:
    print(i,end=" ")