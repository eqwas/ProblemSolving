import sys
#sys.stdin = open("in1.txt", "rt")
a=[list(map(int,input().split())) for _ in range(9)]
"""
yn=1
checklist={1,2,3,4,5,6,7,8,9}
for i in range(9):
    n=set({})
    m=set({})
    for j in range(9):
        n.add(a[i][j])
        m.add(a[j][i])
    if n!=checklist or m!=checklist:
        yn=0
if yn==1:
    print("YES")
else:
    print("NO")
"""

def check(a):
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9)
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True

a=[list(map(int,input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")