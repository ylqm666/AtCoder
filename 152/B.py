a = list(map(int, input().split()))
ans = []

a.sort()
for i in range(a[1]):
    ans.append(a[0])

print(int(''.join(map(str,ans))))
