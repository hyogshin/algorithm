n = int(input())
h = [0] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (3) for _ in range(n+1)]
dp[1] = h[1]
for i in range(2, n+1):
  dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + h[i][0]
  dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + h[i][1]
  dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + h[i][2]

print(min(dp[n]))