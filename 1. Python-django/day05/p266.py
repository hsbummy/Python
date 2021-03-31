import time
import datetime

t = time.time()
print(t);#1970.1.1~현재까지의 초
# locat= time.localtime()
# print(locat.tm_year)
# print(locat.tm_mon)
# print(locat.tm_min)

localtime= datetime.datetime.now()

print(localtime)

