import sys
#sys.stdion = open("in1.txt", "rt")
# n=int(input())
# a=list(map(int,input().split()))
n=10
a=[65,73,66,87,92,67,55,79,75,80]
# ave=0
# for i in a:
#     ave+=i
# ave=round(ave/len(a))
# print(ave)

ave=round(sum(a)/n)
min=2147000000
stuNum=-1

for idx,x in enumerate(a): #a의 index와 값 모두 받아오기
    tmp=abs(x-ave) # 절대값으로 거리구하기
    if tmp<min:
        min=tmp
        score=x
        stuNum=idx+1
    elif tmp==min:
        if x>score:
            score=x
            stuNum=idx+1
print(ave,stuNum)