A, B, C, D = map(int, input().split())

while A > 0 or C > 0:
    if C > 0:
        C = C - B

    elif A > 0:
        A = A - D

    else:
        break

if A <= 0:
    print("No")

else:
    print("Yes")