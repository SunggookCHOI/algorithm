import sys,math

a,b,v = map(int,sys.stdin.readline().split())

n = (v-b)/(a-b)
print(math.ceil(n))
