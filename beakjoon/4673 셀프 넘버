# https://www.acmicpc.net/problem/4673
import sys
from collections import defaultdict

dic = defaultdict(int)
def d(n):
    return n + sum(int(s) for s in str(n))
def main():
    for i in range(1,10000):
        dic[d(i)] = dic[d(i)]+1
    for i in range(1,10000):
        if dic[i] ==0:
            print(i)
if __name__ == '__main__':
    main()
