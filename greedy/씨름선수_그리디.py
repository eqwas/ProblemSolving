import sys
#sys.stdin = open("in1.txt", "rt")
n=int(input())
player=[]
for i in range(n):
    t,w=map(int,input().split())
    player.append((t,w))
player.sort(reverse=True)
cnt=0
weight=0
for t,w in player:
    if w>weight:
        weight=w
        cnt+=1

print(cnt)