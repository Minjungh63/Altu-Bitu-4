N, M = map(int, input().split())
sequence = [0 for _ in range(M + 1)]
is_used = [False for _ in range(N)]
cursor = 0


def backtrack(cursor):
    if cursor == M:
        ans = ""
        for j in M:
            ans += str(sequence[j]) + " "
        print(ans)
        return
    for i in range(N):
        if not is_used[i]:
            sequence[cursor] = i + 1
            is_used[i] = True
            return backtrack(cursor + 1)
