H, W = map(int, input().split())

a = H // 2
b = H // 2 + 1
c = W // 2
d = W // 2  + 1


if H == 1 or W == 1:
    print (H * W)

elif H % 2 == 0 and W % 2 == 0:
    print(a * c)

elif H % 2 == 0 and W % 2 != 0:
    print(a * d)

elif H % 2 != 0 and W % 2 == 0:
    print(b * c)

else :
    print(b * d)