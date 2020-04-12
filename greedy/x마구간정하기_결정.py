import sys
#sys.stdin = open("in1.txt", "rt")
n,c = map(int,input().split())
x=[]
for i in range(n):
    x.append(int(input()))
#n : 마굿간 수, c= 말 수, x=마굿간 좌표
def Check(mid):
    tmp=[]
    for i in x:
        if tmp==[]:
            tmp.append(i)
            continue
        if tmp[-1]+mid<=i:
            tmp.append(i)
    return len(tmp)
def Check2(len):
    cnt=1 
    ep=x[0]#말한마리 배치
    for i in range(1,n):
        if x[i]-ep>=len:
            cnt+=1
            ep=x[i]
    return cnt
    
res=0 # 최대거리값
x.sort()
lt=x[0]
rt=x[-1]#두말의 최대거리 
while lt<=rt:
    mid=(lt+rt)//2
    if Check(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)

#12489
"""
lt=1 rt=9 mid=5
tmp[1,8]
lt=1 rt=4 mid=2
tmp[1,4,8]
lt=3 rt=4 mid=3
tmp[1,4,8]
"""

"""
124 1 2 
128 1 6 
129 1 7 
248 2 4 
249 2 5 
489 4 1 
148 3 4 
149 3 5
189 7 1 

"""
"""
답의 범위 : 1~802
중간값 을 구하고 그게 답이되는지 확인한다
ex 400으로 답 확인
답이 안나올 때, 답보다 적으면 rt=mid-1 또 중간값인 200으로 확인
답이상이고 답보다 크면 일단 res에 저장해두고 lt=mid+1
답이상인 값 중 가장 좋은값까지 반복
"""
# 0 1 2 3 4 5 6 7