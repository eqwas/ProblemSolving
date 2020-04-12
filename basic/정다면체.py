import sys
#sys.stdion = open("in1.txt", "rt")
# n=int(input())
# a=list(map(int,input().split()))

n=4
m=6
answer=[0]*(n+m+1)

for i in range(1,n+1):
    for j in range(1,m+1):
        answer[i+j]+=1
max=max(answer)
for i in range(0,len(answer)):
    if answer[i]==max:
        print(i,end=" ")