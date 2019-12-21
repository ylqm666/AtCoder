n = int(input())
s = str(input())
ans = [s[0]]
cnt = 1
for i in range(0,n):
    if s[i] != ans[-1]:
        ans.append(s[i])
        cnt += 1
print(cnt)
