import sys

n=int(sys.stdin.readline())
times = []
for _ in range(n):
    times.append(tuple(map(int,sys.stdin.readline().split())))
  
times.sort()
times.sort(key=lambda x: x[1])
now,ans=0,0
for time in times:
    if time[0]>=now:
        ans+=1
        now=time[1]
print(ans)
