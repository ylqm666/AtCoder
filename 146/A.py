week = ["SUN","MON","TUE","WED","THU","FRI","SAT" ]
 
str = input()
num = week.index(str)
if num == 0:
    print("7")
else:
    print(7-num)