<h1>가장 큰 정사각형 찾기</h1>
출처 : https://programmers.co.kr/learn/courses/30/lessons/12905  <br><br>

<h3>문제 요약</h3>
0과 1로 이루어진 이차원 배열에서 1로 이루어진 가장 큰 정사각형의 크기를 찾아 반환한다. <br><br>

<h3>문제 풀이</h3>
<ol> 모든 (row, col) 에 대해서 사이즈를 늘려가며 체크하면, 효율성이 좋지 않다.</ol>
<ol> 0행과 0열을 제외하고, (1,1) 부터 요소값이 1인 요소의 값을 좌측, 좌측상단, 상단의 세 요소중 최소값에 1을 더한 값으로 바꾼 후, 모든 요소의 값 중 가장 큰값을 제곱하여 반환한다.</ol>
  예를 들어, 좌측, 좌상단, 상단 중 하나라도 0이 있으면 해당 요소의 값은 1이 된다. => 2가 되려면 좌 좌상단, 상단 모두 1이상 이어야 한다.<br>
  즉, 해당 요소를 기준으로 좌상단으로 최대 정사각형의 크기가 n 이려면, 좌, 좌상단, 상단 모두의 각각의 좌상단으로의 정사각형의 길이가 n-1 이상이어야 한다.<br>
<ol> 단, 2와 같이 해결 할 경우, 행이나 열의 크기가 2 이하일 경우 해결할 수 없으므로 따로 예외처리 해준다.</ol>

<h3>실패한 풀이</h3>
def solution(board):

    answer = 0

    xlen = len(board[0])

    ylen = len(board)

    for row in range(ylen):

        for col in range(xlen):

            tempLen = min(ylen-row,xlen-col)

            if ylen-row<=answer  : return answer**2

            if answer>= tempLen : break; 

            if initialCheck(row,col,answer,board) :

                for i in range(answer, tempLen+1):

                    if checkSquare(row,col,i, board):

                        answer = i

                    else : 

                        break;

    return answer**2



def initialCheck(row, col, length, board):

    for i in range(length):

        if sum(board[row+i][col:col+length]) != length:

            return False

    return True



def checkSquare(row, col, length, board):

    if sum(board[row+length-1][col:col+length]) != length :

        return False

    for l in range(length):

        if board[row+l][col+length-1]==0:

            return False

    return True
