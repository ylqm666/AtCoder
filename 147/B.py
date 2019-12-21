s = input()
l = len(s)
n = 0

for i in range(l//2):
    if s[i] != s[l-i-1]:
        n += 1
print(n)