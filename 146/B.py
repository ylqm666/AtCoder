num = int(input())
str_input = input()
str_arr = list(str_input)
 
for i in range(len(str_arr)):
    if ord(str_arr[i]) + num <= ord("Z"):
        str_arr[i] = chr(ord(str_arr[i]) + num)
    else:
        str_arr[i] = chr(ord(str_arr[i]) - ord("Z") + ord("A") + num - 1)
print("".join(str_arr))