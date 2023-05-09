# 入力
N, L = map(int, input().split())
S = [input() for _ in range(N)]

# Sを辞書順で並べる
S.sort()

print("".join(S))

