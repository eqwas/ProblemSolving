import sys
#sys.stdin = open("in1.txt", "rt")
subject=input()
n=int(input())
for x in range(n):
    check=list(input())
    cnt=0
    for i in range(len(check)):
        if check[0] not in subject:
            check.pop(0)
        else:
            check.append(check.pop(0))
    res=''
    for j in check:
        res+=j
    if res==subject:
        print("#{0} YES".format(x+1))
    else:
        print("#{0} NO".format(x+1))
    
        
