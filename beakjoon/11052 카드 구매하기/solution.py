v=int(input())
p=list(map(int,input().split()))
dp = [0]

for n in range(1,v+1):
    dp.append(max(dp[-i-1]+p[i] for i in range(n)))
print(dp)
