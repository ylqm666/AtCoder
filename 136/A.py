a, b, c = map(int, input().split())

ans = a - b
ans = c - ans
if ans <= 0:
    print(0)
else:
    print(ans)