n = list(map(int,input().split()))
h = list(map(int,input().split()))
cnt = 0

for i in range(n[0]):
    if n[1] <= h[i]:
        cnt += 1
print(cnt)