# https://www.acmicpc.net/problem/4344

import sys
readline = sys.stdin.readline

def main(n):
    for _ in range(n):
        nums = list(map(int,readline().split()))
        mean = sum(nums[1:])/nums[0]
        print('%.3f'%(sum(1 for x in nums[1:] if x > mean)*100/nums[0]) + '%')

if __name__ == '__main__':
    n =int(readline())
    main(n)
