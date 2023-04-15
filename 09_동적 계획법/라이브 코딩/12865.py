N, K = map(int, input().split())
dp = [[0 for _ in range(K + 1)] for _ in range(N+1)]

for i in range(1, N + 1):
    W, V = map(int, input().split())
    for j in range(1, K + 1):
        if j < W:
            dp[i][j] = dp[i - 1][j]
        else: # j >= W이면 W가 영향을 주는 범위이므로
            dp[i][j] = max(V + dp[i - 1][j - W], dp[i - 1][j])

print(dp[N][K])
