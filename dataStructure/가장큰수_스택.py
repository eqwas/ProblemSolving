import sys
sys.stdin = open("in1.txt", "rt")
n,m = map(int,input().split())
"""
n=str(n)
cnt=0
tmp=[]
for i in n:
    i=int(i)
    if tmp==[]:
        tmp.append(i)
        continue
    elif tmp[-1]>i:
        tmp.append(i)
        continue
    elif tmp[-1]<i and cnt<m:
        for j in range(len(tmp)):
            if tmp[-1]<i:
                tmp.pop()
                cnt+=1
                if cnt==m:
                    break
    tmp.append(i)
tmp=tmp[:len(n)-m]
for i in tmp:
    print(i,end= " ")
"""
n=list(map(int,str(n)))
stack=[]
for x in n:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
res=''.join(map(str,stack))
print(res)