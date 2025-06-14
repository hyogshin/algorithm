n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1 % 10007)
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n] % 10007)