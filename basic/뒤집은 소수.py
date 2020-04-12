import sys
#sys.stdion = open("in1.txt", "rt")
# n=int(input())
# a=list(map(int,input().split()))
def reverse(x):
    result=0
    while x>0:
        t=x%10 #마지막자리
        result=result *10 +t
        x=x//10
    return result
def isPrime(x):
    if x==1:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    else:
        return True
# 1*1
# 2*10
# 3*100

# 321 
# t=1
# re=0*10+1=1
# x=32

# t=2
# re=1*10+2 = 12
# x=3

# t=3
# re=12*10+3 =123


n=5
a=[32,55,62,3700,250]

for i in a:
    tmp=reverse(i)
    if isPrime(tmp)==True:
        print(tmp,end=" ")