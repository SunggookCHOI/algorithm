code = input()
if code[0] == '0' : print(0)
elif len(code) == 1:
    print(1)
else:
    dp=[1,1]
    check = True
    for i in range(1,len(code)-1):
        if code[i-1:i+1] <= '26' :
            if code[i-1:i+1] == '00':
                dp = [0]
                check = False
                break
            #x y
            if code[i-1] == '0':
                temp = dp[1]
            else :
                #xy
                if code[i] == '0':
                    temp = dp[1]
                #x != 0, y != 0
                else :
                    #xy, x y 둘다 가능
                    if code[i+1] != '0':
                        temp = (dp[0]+dp[1])
                    # x y 만 가능
                    else :
                        temp = dp[1]
        else :
            if code[i] =='0' :
                dp = [0]
                check = False
                break
            else :
                temp = dp[1]
        dp = [dp[1],temp%1000000]
    if check :
        last = code[-2:]
        if last > '26' and last[1] == '0':
            dp = [0]
        elif last <= '26' and last[0] != '0' and last[1] != '0':
            dp = [sum(dp)%1000000]
        elif last == '00' :
            dp = [0]
    print(dp[-1])
