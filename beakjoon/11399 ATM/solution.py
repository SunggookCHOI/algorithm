import sys
n=int(sys.stdin.readline())
p=sorted(list(map(int,sys.stdin.readline().split())))
ans = 0
for i, v in enumerate(p):
    ans+=sum(p[:i])+v
print(ans)
