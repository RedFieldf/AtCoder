# 入力
N, L = map(int, input().split())
S = [input() for _ in range(N)]

# Sを辞書順で並べる
S.sort()

# 連結させた文字列で出力
print("".join(S))

