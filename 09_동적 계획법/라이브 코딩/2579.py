N = int(input())
score = [int(input()) for _ in range(N)]

dp = [0 for _ in range(N)]
dp[0] = score[0]
if N >= 2:
    dp[1] = score[0] + score[1]
if N >= 3:
    dp[2] = max(score[0], score[1]) + score[2]
if N >= 4:
    for i in range(3, N):
        dp[i] = max(dp[i - 2], dp[i - 3] + score[i - 1]) + score[i]

print(dp[N - 1])
