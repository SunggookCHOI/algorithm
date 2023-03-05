//https://school.programmers.co.kr/learn/courses/30/lessons/161990
function solution(wallpaper) {
    var answer = [-1,51,0,0];
    let rSize = wallpaper.length;
    let cSize = wallpaper[0].length;
    
    wallpaper.map(function(row, i){
        const tmp = row.split('');
        const min = tmp.findIndex((e) => e == '#');
        // findLastIndex 함수가 사용 안되서 뒤집어서 맨 뒤의 # 위치 찾기
        const maxTmp = tmp.reverse().findIndex((e) => e == '#');
        const max = (maxTmp != -1) ? cSize - maxTmp : -1
        
        if ( min != -1 && max != -1){
            if ( answer[0] == -1 ){
                answer[0] = i;
            }
            answer[2] = i;
        }
        if ( min != -1 && min < answer[1] ){
            answer[1] = min;
        }
        if ( max != -1 && max > answer[3]){
            answer[3] = max;
        }
    })
    answer[2]++;
    return answer;
}
