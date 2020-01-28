from functools import cmp_to_key

def comparator(x, y):
    if x[1] < y[1] : 
        return 1 
    elif x[1] > y[1] :
        return -1
    else :
        if x[0] < y[0] :
            return -1
        else :
            return 1
            
def solution(genres, plays):
    g_songs = {}
    g_num = {}

    for i in range(len(plays)):
        if genres[i] in g_songs :
            temp= g_songs[genres[i]]
            temp.append([i,plays[i]])
            g_songs[genres[i]] = temp
            g_num[genres[i]] = g_num[genres[i]] + plays[i]
        else :
            g_songs[genres[i]] = [[i,plays[i]]]
            g_num[genres[i]] = plays[i]

    genre_set = list(g_num.keys())
    genre_set.sort(key=lambda el:g_num[el], reverse=True)

    best = []
    
    for g in genre_set:
        temp = sorted(g_songs[g], key=cmp_to_key(comparator))
        if len(temp)==1:
            best.append(temp[0][0])
        else :
            for i in range(2):
                best.append(temp[i][0])
    return best
