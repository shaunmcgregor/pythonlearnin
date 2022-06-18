import math

for x in range(1, 50) : 
    if(x%5) == 0 and (x%3) == 0 :
        print(str(x) + ": fizzbuzz")
    elif (x%3) == 0 :
        print(str(x) + ": fizz")
    elif (x%5) == 0:
        print(str(x) + ": buzz")
    else:
        print(str(x) +": ")

