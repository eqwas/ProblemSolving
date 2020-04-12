import sys
#sys.stdin = open("in1.txt", "rt")
n=int(input())
l=list(map(int,input().split()))
m=int(input())
l.sort()
for i in range(m):
    l[0]+=1
    l[-1]-=1
    l.sort()
print(max(l)-min(l))