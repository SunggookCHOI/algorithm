import re
def solution(user_id, banned_id):
    # 가능한 제재id
    global answer
    answer = []
    # key : banned_id의 id의 index, value : 아래의 checked
    candidate = {}
    for i, b in enumerate(banned_id):
        # re.sub를 활용하여 b의 모든 *을 .으로 변환
        checker = re.compile(re.sub('\*','.',b))
        # banned_id 중 하나인 b에 매칭되는 user_id
        checked = []
        for u in user_id:
            # match가 안되면 결과가 None으로 두번째 조건 만족x
            if len(u) == len(b) and checker.match(u):
                checked.append(u)
        candidate[i] = checked
    # candidate를 활용하여 dfs
    for x in candidate[0]:
        dfs([x],candidate,len(banned_id))
    return len(answer)
'''
selected는 list로 selected[i]는 candidate[i]의 원소 중 하나. 즉 i번째 banned_id에 매칭되는 user_id 중 하나.
n은 banned_id의 길이.
dfs의 탈출 조건은 selected에 들어있는 원소의 수가 n이 되는 것이다.
'''
def dfs(selected,candidate, n):
    # 탈출조건
    if len(selected) == n:
        global answer
        # 중복을 제거하기 위해 selected를 정렬한 후 비교
        tmp = sorted(selected)
        if tmp not in answer:
            answer.append(tmp)
        return ;
    '''
    <selected의 원소 수가 n이 아닌 경우.>
    selected의 원소 수는 다음 banned_id의 index를 의미한다.
    ex) selected에 한개가 들어있으면 banned_id[1](banned_id의 두번째 요소)에 매칭되는 user_id의 집합인 
        candidate[1]의 원소 중 하나를 selected에 넣는다.
    '''
    for x in candidate[len(selected)]:
        if x not in selected:
            dfs(selected+[x],candidate,n)
