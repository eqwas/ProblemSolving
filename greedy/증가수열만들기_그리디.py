import sys
sys.stdin = open("in1.txt", "rt")
from collections import deque
n=int(input())
l=list(map(int,input().split()))
l=deque(l)
"""
cnt=0
now=0
res=""
for i in range(n):
    if l[0]>now and l[-1]>now :
        if l[0]<l[-1]:
            now=l[0]
            cnt+=1
            res+="L"
            l.popleft()
        else:
            now=l[-1]
            cnt+=1
            res+="R"
            l.pop()
    elif l[0]>now and l[-1]<now:
        now=l[0]
        cnt+=1
        res+="L"
        l.popleft()
    elif l[0]<now and l[-1]>now:
        now=l[-1]
        cnt+=1
        res+="R"
        l.pop()
print(cnt)
print(res)
"""
lt=0
rt=n-1
last=0
res=""
tmp=[]
while lt<=rt:
    if l[lt]>last:
        tmp.append((l[lt],'L'))
    if l[rt]>last:
        tmp.append((l[rt],'R'))
    tmp.sort() #튜플의 첫 자료 기준으로 정렬
    if len(tmp)==0:
        break
    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()
print(len(res))
print(res)