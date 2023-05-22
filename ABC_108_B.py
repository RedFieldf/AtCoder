# 入力
x1, y1, x2, y2 = map(int, input().split())

# x軸、y軸の差分を抽出
dif_x = x2 - x1
dif_y = y2 - y1

# 計算
x3 = x2 - dif_y
y3 = y2 + dif_x

x4 = x3 - dif_x
y4 = y3 - dif_y

# 出力
S = [x3, y3, x4, y4]

print(" ".join(map(str, S)))