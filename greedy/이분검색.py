import sys
#sys.stdin = open("in1.txt", "rt")
n,m = map(int,input().split())
a=list(map(int,input().split()))
a.sort()

lt=0
rt=n-1
while True:
    
    p=(lt+rt)//2
    if a[p]==m:
        print(p+1)
        break
    if a[p]>m:
        rt=p-1
        p=p//2
    if a[p]<m:
        lt=p+1

        

# 0 1 2 3 4 5 6 7