n = int(input())
eq = input()
global answer
answer = -2**31

num = []
op = []
for i in range(n):
    if i%2 == 0 :
        num.append(int(eq[i]))
    else :
        op.append(eq[i])

def cal(a,b,oper):
    if oper == '+':
        return a+b
    elif oper == "-" :
        return a-b
    elif oper == "*" :
        return a*b
# num[idx], op[idx] 를 넣는다. 
def dfs(idx, nums, ops):
    global answer
    if idx > len(op):
        stars = [i for i in range(len(ops)) if ops[i]=='*']
        while len(stars) !=0:
            i = stars.pop()
            nums[i]=cal(nums[i],nums[i+1],'*')
            nums.pop(i+1)
            ops.pop(i)
        nomi = nums[0]
        for i in range(len(ops)):
            nomi = cal(nomi,nums[i+1],ops[i])
        if nomi > answer :
            answer = nomi
        return ;
    # 괄호 안치고 넘어간다
    temp_n = nums.copy()
    temp_o = ops.copy()
    temp_n.append(num[idx])
    # 마지막인 경우에는 숫자만 넣어준다
    if idx < len(op) :
        temp_o.append(op[idx])
    dfs(idx+1,temp_n,temp_o)
    #괄호
    if idx <= len(op)-1 :
        temp_n = nums.copy()
        temp_o = ops.copy()
        temp_n.append(cal(num[idx],num[idx+1],op[idx]))
        #마지막인 경우
        if idx < len(op)-1:
            temp_o.append(op[idx+1])
        dfs(idx+2,temp_n,temp_o)
        

dfs(0,[],[])
print(answer)