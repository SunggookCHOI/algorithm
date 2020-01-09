goal, hotel = map(int,input().split())

dic = {}
maxCustomer = 0

for _i in range(hotel):
    co, cu = map(int,input().split())
    if cu in dic:
        dic[cu] = min(dic[cu],co)
    else:
        dic[cu] = co
    if cu > maxCustomer:
        maxCustomer = cu

        
keys = list(dic.keys())

dp = [0]
for i in range(1,maxCustomer+1):
    temp = 1000000001
    for k in keys:
        if k <= len(dp) and dp[len(dp)-k] + dic[k] < temp:
            temp = dp[len(dp)-k] + dic[k]
    dp.append(temp)

for i in range(maxCustomer+1, goal+maxCustomer+1):
    temp = dp[len(dp)-keys[0]] + dic[keys[0]]
    for k in keys[1:]:
        if dp[len(dp)-k] + dic[k] < temp:
            temp = dp[len(dp)-k] + dic[k]
    dp.append(temp)

print(min(dp[goal:]))
