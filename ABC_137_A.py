A, B = map(int, input().split())

c = A + B
d = A - B
e = A * B

if c >= d and c >= e :
    print (c)

elif d >= c and d >= e :
    print (d)

else :
    print (e)
