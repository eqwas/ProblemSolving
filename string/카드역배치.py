import sys
#sys.stdion = open("in1.txt", "rt")
#card=[i for i in range(1,21)]
card=list(range(21))
for _ in range(10): #_일 경우 대입없이 반복된다.
    n,m=map(int,input().split())
    cnt=(m-n+1)//2 #도는 바퀴 수
    for i in range(0,cnt):
        card[(n)+i],card[(m)-i]=card[(m)-i],card[(n)+i]
# for i in range(0,cnt):
#     tmp=card[(n-1)+i]
#     card[(n-1)+i]=card[(m-1)-i]
#     card[(m-1)-i]=tmp
card.pop(0)
for x in card:
    print(x, end=' ')