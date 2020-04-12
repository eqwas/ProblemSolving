import sys
#sys.stdin = open("in1.txt", "rt")
n,m=map(int,input().split())
p=[]
for i in range(1,n+1):
    p.append(i)
cnt=1
while len(p)>1:
    if cnt==m:
        p.pop(0)
        cnt=1
    else:
        p.append(p.pop(0))
        cnt+=1

print(p[0])
