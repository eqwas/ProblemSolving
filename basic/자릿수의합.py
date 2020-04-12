import sys
#sys.stdion = open("in1.txt", "rt")
# n=int(input())
# a=list(map(int,input().split()))

def digit_sum(x):
    total=0
    # for j in str(x):
    #     total+=int(j)
    while x>0:
        total+=(x%10)
        x=x//10
    return total



a=[125,15232,97]

max=-1
answer=-1
digitSum=0
for i in a:
    digitSum=digit_sum(i)
    if digitSum>max:
        max=digitSum
        answer=i

print(answer)