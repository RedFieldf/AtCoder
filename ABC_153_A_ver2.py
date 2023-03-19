H, A = map(int, input().split())

# 攻撃回数を管理する変数
counter = 0

# 体力 H が 0 より大きい限り反復を繰り返す
while H > 0:

    # H から A を引く
    H -= A

    # 攻撃回数を 1 増やす
    counter += 1

print(counter)
