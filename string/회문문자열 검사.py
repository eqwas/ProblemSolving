import sys
#sys.stdion = open("in1.txt", "rt")
n=int(input())
 
 #a=list(map(int,input().split()))
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#{0} NO".format(i+1))
            break
    else:
        print("#{0} YES".format(i+1))

"""
for i in range(n):
    s=input()
    s=s.upper()
    if s==s[::-1]: #s[::-1] 문자열뒤집기
"""

    # a="level"
# b=""
# for i in range(len(a)-1,-1,-1):
#     b+=a[i]
# if b==a:
    