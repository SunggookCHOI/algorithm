# https://programmers.co.kr/learn/courses/30/lessons/77485
def solution(rows, columns, queries):
    answer = []
    v=0
    matrix = []
    # 초기행렬 행성
    for r in range(rows):
        tmp=[]
        for c in range(columns):
            v+=1
            tmp.append(v)
        matrix.append(tmp)
    for query in queries :
        answer.append(rotate(matrix, query))
    return answer

# 행렬을 회전하며 회전한 요소 중 최솟값 반환
def rotate(matrix, query):
    r1,c1,r2,c2=[q-1 for q in query]
    tmp=matrix[r1][c1]
    minn = tmp
    for c in range(c1+1,c2+1):
        tmp2=matrix[r1][c]
        matrix[r1][c] = tmp
        tmp=tmp2
        minn=min(minn,tmp)
    for r in range(r1+1,r2+1):
        tmp2=matrix[r][c2]
        matrix[r][c2] = tmp
        tmp=tmp2
        minn=min(minn,tmp)
    for c in range(c2-1,c1-1,-1):
        tmp2=matrix[r2][c]
        matrix[r2][c] = tmp
        tmp=tmp2
        minn=min(minn,tmp)
    for r in range(r2-1,r1-1,-1):
        tmp2=matrix[r][c1]
        matrix[r][c1] = tmp
        tmp=tmp2
        minn=min(minn,tmp)
    return minn
