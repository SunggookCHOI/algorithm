def solution(N):
    dp = [1,1]
    for i in range(2,N):
        dp.append(dp[-1]+dp[-2])
    if N==1 : return 4
    return (2*dp[-1])+(2*(dp[-2]+dp[-1]))
