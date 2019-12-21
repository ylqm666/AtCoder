num = int(input())
ans = "No"
for i in range(1,10):
    if num % i == 0 and num//i < 10:
        ans = "Yes"
print(ans)