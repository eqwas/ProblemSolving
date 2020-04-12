import sys
sys.stdin = open("in1.txt", "rt")
#from collections import deque
n=int(input())
l=list(map(int,input().split()))
"""
tmp=[]
cnt=n
for i in range(n,0,-1):
    tmp.insert(l[i-1],cnt)
    cnt-=1
for i in tmp:
    print(i,end=" ")

"""
seq=[0]*n
for i in range(n):
    for j in range(n):
        print(l)
        print(seq)
        if l[i]==0 and seq[j]==0:
            seq[j]=i+1
            break
        elif seq[j]==0:
            l[i]-=1
for x in seq:
    print(x,end=' ')