import sys

def solve(hh,mm):
  mm -= 45
  if mm < 0 :
    mm += 60
    hh -= 1
    if hh >= 0:
      return hh,mm
    else :
      return 23,mm
  else :
    return hh,mm

if __name__=='__main__':
  hh,mm = map(int,sys.stdin.readline().split())
  nh, nm = solve(hh,mm)
  print(nh,nm)
