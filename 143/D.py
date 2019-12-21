from bisect import bisect_left
n = int(input())
l = list(map(int,input().split()))
l.sort()
cnt = 0

for i in range(0,n-2):
    for j in range(i+1,n-1):
        cnt += bisect_left(l,l[i]+l[j])-j-1

print(cnt)