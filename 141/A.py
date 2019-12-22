input_wtr = str(input())
wtr = ['Sunny','Cloudy','Rainy']

if input_wtr == wtr[-1]:
    print(wtr[0])
else:
    print(wtr[wtr.index(input_wtr)+1])