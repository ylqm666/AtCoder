n, k, q = map(int, input().split())
points = [0] * n
for i in range(q):
    a = int(input())
    points[a - 1] += 1

for j in points:
    if q-j >= k:
        print('No')
    else:
        print('Yes')