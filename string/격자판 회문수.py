import sys
#sys.stdin = open("in1.txt", "rt")
def isH(a):
    for i in range(len(a)//2):
        if a[i]!= a[len(a)-1-i]:
            return False
    return True

a=[list(map(int,input().split())) for _ in range(7)]
cnt=0
"""
for i in range(7):
    tmp=[]
    for j in range(3):
        tmp=a[i][j:j+5]
        if isH(tmp):
            cnt+=1
for i in range(7):
    tmp=[]
    for j in range(7):
        tmp.append(a[j][i])

    for k in range(3):
        if isH(tmp[k:k+5]):
            cnt+=1

print(cnt)
"""
for i in range(3):
    for j in range(7):
        tmp=a[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        for k in range(2): #열의 회문비교 두번만비교하면 되니까 2 
            if a[i+k][j]!=a[i+5-k-1]:
                break
        else:
            cnt+=1
print(cnt)