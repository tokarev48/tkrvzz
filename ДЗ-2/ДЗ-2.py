# -- coding: utf-8 --
import math
x = 1.825 * 100
y = 18.225
z = -3.298*0.01
s = math.fabs(x**(y/x)-(y/x)**1/3) + (y-x)*((math.cos(y)-z/(y-x))/(1+(y-x)**2))
print(s)