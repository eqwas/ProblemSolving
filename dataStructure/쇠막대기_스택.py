import sys
sys.stdin = open("in1.txt", "rt")
n=input()
n=list(n)
"""
cnt=0
bar=0
now=''
while n:
    if n[-1]==')' and n[-2]=='(':
        cnt+=bar
        n.pop()
        n.pop()
    elif n[-1]==')':
        cnt+=1
        bar+=1
        n.pop()
    elif n[-1]=='(':
        n.pop()
        bar-=1


print(cnt)
"""
tmp=[]

sum=0
for i in n:
    if i=='(':
        tmp.append(i)
    elif i==')':
        tmp.pop()
        if tmp[-1]=='(':
            #tmp.pop()
            sum+=len(tmp)
        else:
            #tmp.pop()
            sum+=1
print(sum)

