import bankapi
from bankapi import Account

acc = Account('1111', 10000, 3.4)
print(acc)
try:
    acc.withdraw(20000)
except ValueError:
    print("잔고가 부족합니다.")
except bankapi.MinusError:
    print("입력금액이 오류")
print(acc)


# except BaseException as b:
#     if b.args[0] == "111":
#         print('입력금액이 음수 입니다.')
#     else:
#         print("잔액 부족입니나.")