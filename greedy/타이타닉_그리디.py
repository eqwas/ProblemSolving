import sys
sys.stdin = open("in3.txt", "rt")
from collections import deque

n,m = map(int,input().split())
l=list(map(int,input().split()))
l.sort()
cnt=0
l=deque(l)
"""
while l!=[]:
    if l[-1]+l[0]>m or len(l)==1:
        l.pop()
        cnt+=1
    elif l[-1]+l[0]<=m:
        l.pop()
        l.pop(0)
        cnt+=1
        """
while l!=[]:
    if len(l)==1:
        cnt+=1
        break
    if l[-1]+l[0]>m:
        l.pop()
        cnt+=1
    elif l[-1]+l[0]<=m:
        l.pop()
        l.popleft() #데큐를 통해 좀 더 효율적인 연산이 가능하다.
        cnt+=1
print(cnt)

#50 60 70 90 100
