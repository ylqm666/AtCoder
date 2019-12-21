n = int(input())
nr = int(n ** 0.5) + 1
for i in range(nr,0,-1):
    if n % i == 0:
        j = n // i
        break
print(i + j -2)
