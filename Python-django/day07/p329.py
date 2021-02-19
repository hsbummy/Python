# car = ['c001','k1',1000,50,30]
#
# class Car:
#     def __init__(self,id ,name, size, fsize, cfsize):
#         self.id = id
#         self.name = name
#         self.size = size



# account = ['01044445555',10000, 5.8]
#
# accM = account[1]
# accM += 1000
# account[1] = accM

import math

math.cos(34)

class Account:
    def __init__(self, accNO, balance, rate):
        self.accNo = accNO
        self.balance = balance
        self.rate = rate

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money

    def inquire(self):
        return self.balance

acc1 = Account('111', 20000,4.5)
print("잔액은 {0} 원 입니다.".format(acc1.inquire()))

acc1.deposit(10000)
print("잔액은 {0} 원 입니다.".format(acc1.inquire()))




