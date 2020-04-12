import sys
#sys.stdin = open("in1.txt", "rt")

n,m = map(int,input().split())
a=list(map(int,input().split()))
def Count(len):
    cnt=1
    tmp=0
    for i in a:
        if(tmp+i>len):
            #tmp=0
            tmp=i
            cnt+=1
        else:
            tmp+=i
    return cnt
maxx=max(a) #이게 없으면 위 tmp=i에서 dvd용량이 노래용량보다 작은데 그냥 넣어버리게됨
largest=(sum(a)) 
lt=1
rt=largest
res=0 #dvd최소용량크기
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m: #dvd용량은 최소한 가장 용량이 큰노래보다는 무조건 커야함
        res=mid
        rt=mid-1
    if Count(mid)>m:
        lt=mid+1
print(res)
    


# lt=1, rt=45 mid = 23
#1,2,3,4,5,6/7,8/9 cnt=3
#cnt==k: res=23, rt=23-1=22
#lt=1,rt=22,mid=11
#1,2,3,4/5,6/7/8/9 cnt=5
#cnt>k: lt=11+1
#lt=12,rt=22,mid=16
#1,2,3,4,5/6,7/8/9 cnt=4
#cnt>k: lt=16+1=17
#lt=17,rt=22 mid=19


"""
답의 범위 : 1~802
중간값 을 구하고 그게 답이되는지 확인한다
ex 400으로 답 확인
답이 안나올 때, 답보다 적으면 rt=mid-1 또 중간값인 200으로 확인
답이상이고 답보다 크면 일단 res에 저장해두고 lt=mid+1
답이상인 값 중 가장 좋은값까지 반복
"""
# 0 1 2 3 4 5 6 7