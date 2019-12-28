def solution(N, road, K):
    distance = [500001 for i in range(N)]
    distance[0]=0
    queue = [[1,0]]
    while len(queue) != 0:
        
        present = queue.pop(0)
        for r in road :
            if r[0] == present[0] :
                if distance[r[1]-1]> present[1]+r[2]:
                    distance[r[1]-1]= present[1]+r[2]
                    queue.append([r[1], present[1]+r[2]])
            elif r[1] == present[0] : 
                if distance[r[0]-1]> present[1]+r[2]:
                    distance[r[0]-1]= present[1]+r[2]
                    queue.append([r[0], present[1]+r[2]])
                
    return len([x for x in distance if x<=K])
