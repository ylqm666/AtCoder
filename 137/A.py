a, b = map(int, input().split())
ans_list = [] *3
ans_list.append(a+b)
ans_list.append(a-b)
ans_list.append(a*b)

print(max(ans_list))