import sys
#sys.stdin = open("in1.txt", "rt")
n=int(input())
use=[]
for i in range(n):
    use.append(input())
for i in range(n-1):
    use.remove(input())
print(use[0])