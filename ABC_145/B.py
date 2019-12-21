input_num = int(input())
input_str = str(input())
 
if input_num % 2 == 0 and input_str[:input_num//2] == input_str[input_num//2:]:
    print ("Yes")
else:
    print ("No")