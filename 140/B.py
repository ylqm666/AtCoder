n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

for i in range(n-1):
    if a[i] == a[i+1]-1:
        b.append(c[a[i]-1])
print(sum(b))