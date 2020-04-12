import sys
#sys.stdion = open("in1.txt", "rt")
n=int(input())
a=list(map(int,input().split()))

# n=10
# a=[1,0,1,1,1,0,0,1,1,0]
res=0
cnt=1
for i in a:
    if i==1:
        res+=cnt
        cnt+=1
    if i==0:
        cnt=1
print(res)