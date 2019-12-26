n = int(input())
s,t = input().split()

str_ans = ''

for i in range(n):
    str_ans += s[i]
    str_ans += t[i]
print(str_ans)