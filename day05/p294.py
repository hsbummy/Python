# d ='a'
# result = 0
# try:
#     num = int(d)
#     result=10 / num
#     print(result)
# except ValueError as e:
#     print(e.with_traceback())
#     print('invalid data')
#     exit()
# except ZeroDivisionError as z:
#     print('zero no')
#     exit()

d = 10
result = 0
try:
    num = int(d)
    result = 10/num
    print(result)
except ValueError:
    print('wrong')
    exit()
except ZeroDivisionError:
    print('z')
    exit()