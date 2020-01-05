import sys

def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)

n = int(input())
minB = pow(10,18)
lastB = 0
pay = None

valid = True
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    if a+lastB<0:
        temp = b-a-lastB
        if b != 0 and b<minB : minB=b
        if pay == None:
            pay = temp
        else :
            pay = gcd(pay,temp)
            if pay <= minB and minB != pow(10,18):
                valid = False
                break
    else:
        if lastB + a != b:
            valid = False
            break
    lastB = b
if valid and pay != None : print(pay)
elif valid and pay == None : print(1)
else : print(-1)
