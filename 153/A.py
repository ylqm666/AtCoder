h, n = map(int,input().split())
ans = int(h // n)
if h % n:
    ans += 1
print(ans)
