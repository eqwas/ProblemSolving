import sys
#sys.stdion = open("in1.txt", "rt")
# n=int(input())
# a=list(map(int,input().split()))

n=20
cnt=0
a=[0]*(n+1)
for i in range(2,n+1):
    if a[i]==0:
        cnt+=1
        for j in range(i,n+1,i):#i만큼 더한다
            a[j]=1

print(cnt)
#2가 소수라면 1으로 체크하고, 2의배수들은 전부 소수가 아니라고 1로체크
