a, b, x = map(int,input().split())
max = 10**9 + 1
min = 0
while max - min > 1:
    mid = (max + min) // 2
    if x < (a * mid) + (b * len(str(mid))):
        max = mid
    else:
        min = mid

print(min)
