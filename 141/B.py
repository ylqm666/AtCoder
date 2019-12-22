input_tap = input()
flag = 'No'
input_tap1 = input_tap[0::2]
input_tap2 = input_tap[1::2]

if 'L' in input_tap1:
    flag = 'No'
elif 'R' in input_tap2:
    flag = 'No'
else:
    flag = 'Yes'
print(flag)
