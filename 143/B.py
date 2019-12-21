n = int(input())
tako = list(map(int, input().split()))
sum = 0

for i in range(0,n-1):
    for j in range(i+1,n):
        hp = tako[i] * tako[j]
        sum += hp
print(int(sum))
