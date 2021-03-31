from myutil1 import calc
from myutil1 import input

# d = 1000
# try:
#     result = calc(d)
#     print(result)
# except ValueError:
#     print('Value')
#     exit()

# except ZeroDivisionError:
#     print('zero')
#     exit()
#
# try:
#     result = input(d)
#     print('입력금액은 %s 입니다.' % (result))
# except ValueError:
#     print('wrong')
#     exit()

d = 10000
# result = input(d)
# if result == 1:
#     print('입력금액은 %s ' % (result))
# else:
#     print('숫자를 잘못 입력')

try:
    result = input(d)
    print('입력금액은 %s' % (result))
except:
    print('숫자가잘못입력')