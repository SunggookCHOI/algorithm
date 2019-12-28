def solution(money):
    if len(money)==3:
        return max(money)
    
    from0 = [0 for i in range(len(money))]
    from1 = [0 for i in range(len(money))]
    
    from0[0] = money[0]
    from0[2] = from0[2-2]+money[2]
    from1[1] = money[1]
    from1[2+1] = from1[2-2+1]+money[2+1]
    for i in range(3,len(money)-1): 
        # (전전집+이번집 털기, 전집 털기)
        from0[i] = max(from0[i-2]+money[i], from0[i-1], from0[i-3]+money[i])
        from1[i+1] = max(from1[i-2+1]+money[i+1], from1[i-1+1], from1[i-3+1]+money[i+1])
    
    
    return max(from0[-2],from1[-1], from0[-3]-money[0]+money[-1])
