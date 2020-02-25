def solution(string):
    stack = []
    for s in string:
        if s=='(' or s=='[':
            stack.append(s)
        elif s==')':
            if len(stack)>0 and stack[-1]=='(':
                stack.pop()
            else:
                return 'no'
        elif s==']':
            if len(stack)>0 and stack[-1]=='[':
                stack.pop()
            else:
                return 'no'
    return 'yes' if len(stack)==0 else 'no'

import sys
if __name__=='__main__':
    while 1:
        string = sys.stdin.readline()[:-1]
        if string == '.':
            break
        print(solution(string[:-1]))
