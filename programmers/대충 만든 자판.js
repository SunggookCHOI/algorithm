//https://school.programmers.co.kr/learn/courses/30/lessons/160586?language=javascript
function solution(keymap, targets) {
    let answer = [];
    
    // 알파벳 : 입력을 위한 최소 입력
    let dictObj = {};
    
    // 특정 알파벳을 입력하기 위한 키보드 최소 입력값
    keymap.forEach(keys => {
        keys.split('').map(function(k,i){
            if ( k in dictObj ){
                dictObj[k] = Math.min(dictObj[k], i+1);
            } else {
                dictObj[k]=i+1;
            }
        })
    })
    
    targets.forEach(target => {
        answer.push(count(dictObj,target));
    })
    
    return answer;
}

// 문자열 target을 작성하기 위해 필요한 키보드 입력 횟수 반환
function count(keymap, target){
    let answer = 0;
    for (t of target.split('')){
        if ( t in keymap ){
            answer += keymap[t];
        } else {
            return -1;
        }
    }
    return answer;
}
