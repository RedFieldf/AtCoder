X = int(input())

saving = 100
year = 0

while saving < X:
    saving = (saving * 101) // 100
    year += 1

print(year)