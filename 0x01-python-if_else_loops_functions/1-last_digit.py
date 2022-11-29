#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if(number < 0):
    lat = int(str(number)[-1]) * -1
else:
    lat = int(str(number)[-1])
if lat > 5:
    print("Last digit of",number, "is" ,lat, "and is greater than 5")
elif lat == 0:
    print('Last digit of',number, 'is' ,lat, 'and is 0')
else:
    print("Last digit of" ,number, "is" ,lat, "and is less than 6 and not 0")
