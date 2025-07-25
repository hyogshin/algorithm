from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if not visited[nx][ny] and graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y] + 1
          visited[nx][ny] = True
          q.append((nx, ny))

bfs(0, 0)
print(graph[n-1][m-1])