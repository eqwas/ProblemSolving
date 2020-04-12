import sys
#sys.stdin = open("in1.txt", "rt")
def Count(len):
    cnt=0
    for x in line:
        cnt+=(x//len)
    return cnt

k,n = map(int,input().split())
#a=list(map(int,input().split()))
line=[]
res=0
largest=0
for i in range(k):
    tmp=int(input())
    line.append(tmp)
    largest=max(largest,tmp)

lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    if Count(mid)<n:
        rt=mid-1
print(res)



"""
답의 범위 : 1~802
중간값 을 구하고 그게 답이되는지 확인한다
ex 400으로 답 확인
답이 안나올 때, 답보다 적으면 rt=mid-1 또 중간값인 200으로 확인
답이상이고 답보다 크면 일단 res에 저장해두고 lt=mid+1
답이상인 값 중 가장 좋은값까지 반복
"""
# 0 1 2 3 4 5 6 7