n = int(input())
a = list(map(int, input().split()))

cnt = 0
pointer = 1

for i in range(n):
    if a[i] == pointer:
        pointer += 1
    else:
        cnt += 1
if pointer == 1:
    print(-1)
else:
    print(cnt)
