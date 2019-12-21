a, b = map(int, input().split())

if a < b * 2:
    print("0")
else:
    ans = a - b * 2
    print(ans)