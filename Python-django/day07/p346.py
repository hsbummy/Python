import math
from decimal import Decimal
from fractions import Fraction
from array import array

n = 0.1
n = Decimal(str(n))

sum = 0

for i in range(10):
    sum += n

print(sum)


result = 1/3
result = round(result,)
print(result)

resultf1 = Fraction(1,3)
resultf2 = Fraction(1,4)
print(resultf1)
print(resultf2)
print(resultf1 + resultf2 + 0.0)

ar = array('i',[1,2,3,4,8,7,5,6,5,9,8,7])
ar[1] = 100
ar.append(200)
del ar[0]
# ar= ar[3:5]


for i in ar:
    if i%2 == 0:
        print(i, end=" ")