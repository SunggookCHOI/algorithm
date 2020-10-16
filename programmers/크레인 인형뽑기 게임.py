from collections import deque

def solution(board, moves):
    answer = 0
    q = deque()
    board.insert(0, [0 for i in board[0]])
    for m in moves:
        m -= 1
        y = get_top(board, m)
        # 들어 있으면
        if y:
            doll = board[y][m]
            board[y][m] = 0
            if q:
                tmp = q.pop()
                if doll == tmp:
                    answer += 2
                    continue
                else:
                    q.append(tmp)
                    q.append(doll)
            else:
                q.append(doll)
    return answer
# 들어 있으면, 인형의 높이를 반환
def get_top(board, idx):
    for i, v in enumerate(board):
        if v[idx] != 0:
            return i
    return 0
            
