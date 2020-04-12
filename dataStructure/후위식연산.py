import sys
#sys.stdin = open("in1.txt", "rt")
n=input()
n=list(n)
num=[]
res=0
for i in n:
    if i.isdecimal():
        num.append(i)
    else:
        a=int(num.pop())
        b=int(num.pop())
        if i=='+':
            res=b+a
        elif i=='-':
            res=b-a
        elif i=='*':
            res=b*a
        if i=='/':
            res=b/a
        num.append(res)
print(res)