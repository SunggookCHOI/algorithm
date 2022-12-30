# https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=javascript

function solution(t, p) {
    var answer = 0;
    for (var i = 0 ; i < t.length-p.length+1 ; i++){
        var tmp = t.substr(i, p.length);
        if (tmp <= p){
            answer++;
        };
    };
    return answer;
}
