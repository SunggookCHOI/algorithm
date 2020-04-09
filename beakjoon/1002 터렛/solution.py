import sys, math
def solution(x1,y1,r1,x2,y2,r2):
  if x1 == x2 and y1 == y2 :
    if r1 == r2:
      return -1
    else :
      return 0
  
  dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
  r = min(r1,r2)
  R = max(r1,r2)
  s = r + R

  #떨어져서 또는 큰원 안에 작은 원
  if dist > s or (dist + r < R): return 0

  #내접, 내접
  elif dist + r == R or dist == s: return 1

  #위에
  #elif (dist == r and R < 2*r) or dist == R: return 2
  else : return 2



if __name__=="__main__":
  n = int(sys.stdin.readline())
  for _ in range(n):
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().split())
    print(solution(x1,y1,r1,x2,y2,r2))
