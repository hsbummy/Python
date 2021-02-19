# try:
#     print('start.......')
#     data = input('input number.....?')
#     result = int(data) * 1000
#     print(result)
#
# except:
#     print('잘못된 값을 입력하셨습니다.')
#
#
# print('end.......')

#
# print('start.......')
#
# while True:
#     data = input('input number.....?')
#     if data.lower() == 'q':
#         print('BYE..!');
#         exit()
#     if data.isdecimal():
#         result = int(data) * 1000
#         print(result)
#
#     else:
#         print('invalid number type.. try again')
#
#
# print('end.......')
#

#data.isalnum() 숫자 또는 문자냐


print("start")

while True:
    data = input("input number...q")
    if data.lower()=='q':
        print("bye")
        exit()
    if data.isdecimal():
        result = int(data)*1000
        print(result)

    else:
        print('invalid number type..try again')

print('end')