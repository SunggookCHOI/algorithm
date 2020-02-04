import sys
n=int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

dp = [nums[0]]

for i in range(1,n):
    dp.append(max(dp[-1]+nums[i],nums[i]))
print(max(dp))
