n = int(input())
ns = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
  for j in range(i):
    if ns[j] < ns[i]:
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))