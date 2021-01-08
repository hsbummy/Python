# 1. 한 자리 숫자를 입력 받는다.
# 2. 숫자의 범위는 1~9
# 3. 아니면 프로그램 종료
#

# 이거는 내가 한거
# a = input("input number..?")
# sum = 0;
# cnt = 0;
#
# for n in range(1, int(a)+1):
#     sum += int(n)
#     cnt = int(n)
# #
# if 0 < int(a) < 10:
#     print("pass")
# else:
#     exit()
#
# print(sum);
# print(sum/cnt)
#

# a = input('input number...?');
# sum = 0;
# cnt = 0
# for n in range(int(a)):
#     sum += (n+1)
#     cnt += 1
#
# print(sum)
# print(sum/cnt)

# 1. 한 자리 숫자를 입력 받는다.
# 2. 숫자의 범위는 1~9
# 3. 아니면 프로그램 종료

a = input("input number..?")


for x in range(1, int(a)+1):
    if 1 <= int(a) < 11:
        print(x)
    else:
        exit()


