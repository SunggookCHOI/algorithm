n = int(input())
t = []
p = []
for i in range(n):
    a, b = map(int, input().split(' '))
    t.append(a)
    p.append(b)

d=[0 for i in range(n+1)]

for i in range(n+1):
    for j in range(i):
        d[i] = max(d[i],d[j])
        if j+t[j]==i :
            d[i] = max(d[i],d[j]+p[j])
print(max(d))
