import sys
def bf(n,edge):
  INF = 999999999
  dist = [0,0] + [INF for _ in range(n-1)]
  
  for count in range(1,n+1):
    for a in range(1,n+1):
      if dist[a] != INF :
        for b,c in edge[a].items():
          if dist[b] > dist[a]+c :
            dist[b] = dist[a]+c
            if count == n:
              print(-1)
              return
  for a in range(2,n+1):
    print(dist[a] if dist[a] != INF else -1)


if __name__=="__main__":
  n,m = map(int,sys.stdin.readline().split())
  edge = {}
  for a in range(1,n+1):
    edge[a]={}
  for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    edge[a][b]= min(c,edge[a][b]) if b in edge[a] else c
  bf(n,edge)
