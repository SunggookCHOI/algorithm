def solution(board):
    answer = 0
    xlen = len(board[0])
    ylen = len(board)
    if xlen <2 or ylen<2:
        for i in range(ylen):
            if(sum(board[i])>0):
                return 1;
            return 0
    
    for row in range(1,ylen):
        for col in range(1,xlen):
            if board[row][col]==1:
                temp = min(board[row-1][col-1],board[row-1][col], board[row][col-1])+1
                board[row][col] = temp
                if temp > answer:
                    answer = temp
    return answer**2
