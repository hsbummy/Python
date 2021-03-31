# 내 것

# try:
#     a = int(input("input number:?"))
#     b = int(input("input number...?"))
#     c = int(input("input number...?"))
#
# except :
#     print("fail")
#     exit()
#
#
# sum = int(a) + int(b) + int(c)
# avg = sum /3
#
# print(sum)
# print(avg)


# #강사님
#
# print("Start")
# sum = 0;
# avg = 0.0;
# a = (input("input number:?"))
# b = (input("input number...?"))
# c = (input("input number...?"))
#
# try:
#     a_1 = int(a)   # a = int(a) 스트링에서 정수로 변함
#     b_1 = int(b)
#     c_1 = int(c)
# except:
#     print("Invalid Input Data.. Try Again")
#     exit();
# sum = a_1 + b_1 + c_1
# avg = sum / 3
#
# print(a + b + c)
# print(sum)
# print(avg)   # print(sum / 3) # print(round(sum/3,2)) 원데이터를 남겨둬야 한다.
#
# print("End")

print("Start")

sum = 0
avg = 0

a = (input("Input number..?"))
b = (input("Input number..?"))
c = (input("Input number..?"))

try:
    a_1 = int(a)
    b_1 = int(b)
    c_1 = int(c)
except:
    print("Invalid number")
    exit()

sum = a_1 + b_1 + c_1
avg = sum / 3

print(sum)
print(round(avg,2))




# print("Start")

# sum = 0
# avg = 0.0
#
# a = input("input number...?")
# b = input("input number...?")
# c = input("input number...?")
#
# try:
#     a1 = int(a)
#     b1 = int(b)
#     c1 = int(c)
#
# except:
#     print("error")
#     exit()
#
# sum = a1 + b1 + c1
# avg = sum/ 3
#
# print(sum)
# print(avg)