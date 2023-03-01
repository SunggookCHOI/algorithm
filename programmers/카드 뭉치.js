//https://school.programmers.co.kr/learn/courses/30/lessons/159994

function solution(cards1, cards2, goal) {
    return dfs(cards1, cards2, goal);
}

function dfs(cards1, cards2, goal){
    if ( goal.length == 0){
        return 'Yes'
    }
    if ( cards1[0] == goal[0]){
        return dfs(cards1.slice(1), cards2, goal.slice(1));
    }
    if ( cards2[0] == goal[0]){
        return dfs(cards1, cards2.slice(1), goal.slice(1));
    }
    return 'No'
};
