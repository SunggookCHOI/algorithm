import sys, math
def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)
def solution(g,l):
    ans = (l,l)
    temp = (0,0)
    for A in range(math.ceil(math.sqrt(l//g)),0,-1):
      if l%(g*A) == 0:
        B = l//(g*A)
        temp = (A*g,B*g)
        if gcd(A,B) == 1 and sum(temp) < sum(ans):
          ans = temp
                
    print(min(ans),max(ans))
if __name__ == "__main__":
    g,l = map(int,sys.stdin.readline().split())
    solution(g,l)
