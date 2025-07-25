t = int(input())
dp = [0] * (12)
dp[1] = 1
dp[2] = 2
dp[3] = 4

def fibo(n):
  for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
  return dp[n]

for _ in range(t):
  n = int(input())
  fibo(n)
  print(dp[n])