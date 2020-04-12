import sys
#sys.stdin = open("in1.txt", "rt")
n,m=map(int,input().split())
li=list(map(int,input().split()))
max=sorted(li)

cnt=0
while True:
 
    if li[0]==max[-1] and m==0:
        cnt+=1
        break 
    if li[0]==max[-1]:
        li.pop(0)
        max.pop()
        cnt+=1
        if (m-1)<0:
            m=m+n
        else:
            m=m-1
    else:
        li.append(li.pop(0))
        if (m-1)<0:
            m=m+len(li)-1
        else:
            m=m-1

print(cnt)