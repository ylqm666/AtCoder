n = int(input())
a = list(map(int, input().split()))
ans = 0


for i in range(n):
    a[i] = float(1 / a[i])
    ans += a[i]

ans = 1 / ans
print(ans)
