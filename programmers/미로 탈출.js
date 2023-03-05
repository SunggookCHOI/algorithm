//https://school.programmers.co.kr/learn/courses/30/lessons/159993
function solution(maps) {
    var answer = 0;
    let start = [0,0];
    let end = [0,0];
    let lever = [0,0];
    // S, L, E 좌표 탐색
    maps.map(function(row, i){
        let chk = 0;
        row.split('').map(function(r, j){
            if ( r == 'S' ){
                start = [i,j];
                chk += 1;
            }
            if ( r == 'E'){
                end = [i,j];
                chk += 1;
            }
            if ( r == 'L'){
                lever = [i,j];
                chk +=1
            }
            if ( chk == 3 ){
                return ;
            }
        })
        if ( chk ==3 ){
            return ;
        }
    })
    
    // S -> L 시간
    let a = dij(maps, start[0], start[1], lever[0], lever[1]);
    if ( a == 10001){
        return -1;
    }
    
    // L -> E 시간
    let b = dij(maps, lever[0], lever[1], end[0], end[1]);
    
    if ( b != 10001){
        return a+b;
    }else {
        return -1;
    }
}

// (r,c) -> (tr,tc) 걸리는 시간 반환
function dij(maps, r, c, tr, tc){
    let chk = Array.from(Array(maps.length), () => Array(maps[0].length).fill(0));
    let dist = Array.from(Array(maps.length), () => Array(maps[0].length).fill(10001));
    
    dist[r][c] = 0;
    
    let q = [[r,c]];
    while (q.length>0){
        let n = q.shift();
        if ( n[0]>0 && chk[n[0]-1][n[1]] == 0 && maps[n[0]-1][n[1]] != 'X'){
            dist[n[0]-1][n[1]] = Math.min(dist[n[0]][n[1]] + 1)
            chk[n[0]-1][n[1]] = 1;
            q.push([n[0]-1,n[1]]);
        }
        if ( n[0]<maps.length-1 && chk[n[0]+1][n[1]] == 0 && maps[n[0]+1][n[1]] != 'X'){
            dist[n[0]+1][n[1]] = Math.min(dist[n[0]][n[1]] + 1)
            chk[n[0]+1][n[1]] = 1;
            q.push([n[0]+1,n[1]]);
        }
        if ( n[1]>0 && chk[n[0]][n[1]-1] == 0 && maps[n[0]][n[1]-1] != 'X'){
            dist[n[0]][n[1]-1] = Math.min(dist[n[0]][n[1]] + 1)
            chk[n[0]][n[1]-1] = 1;
            q.push([n[0],n[1]-1]);
        }
        if ( n[1]<maps[0].length-1 && chk[n[0]][n[1]+1] == 0 && maps[n[0]][n[1]+1] != 'X'){
            dist[n[0]][n[1]+1] = Math.min(dist[n[0]][n[1]] + 1)
            chk[n[0]][n[1]+1] = 1;
            q.push([n[0],n[1]+1]);
        }
    }
    return dist[tr][tc]
}
