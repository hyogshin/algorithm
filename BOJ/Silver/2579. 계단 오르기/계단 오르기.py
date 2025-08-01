n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n+1)
dp[0] = 0
dp[1] = stairs[1]
if n >= 2:
  dp[2] = stairs[1]+stairs[2]

for i in range(3, n+1):
  dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])

print(dp[n])