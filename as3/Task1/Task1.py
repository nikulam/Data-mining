import math

#lift: xc / x / ad

a = 0.5
b = 0.048
c = 0.203
d = 0.052
e = 0.197

f = 0.251 #XQ
g = 0.249 #XnQ
h = 0.1 #XC
i = 0.4 #XnC

up = a**a * b**b * c**c * d**d * e**e
down = f**f * g**g * h**h * i**i

MI = math.log(up / down, 2)
print(1000*MI)

