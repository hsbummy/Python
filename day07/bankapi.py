class Account:
    def __init__(self, accNO, balance, rate):
        self.__accNo = accNO
        self.__balance = balance
        self.__rate = rate
    def __str__(self):
        return self.__accNo+ " " + str(self.__balance) + ' ' + str(self.__rate) + " " + str(self.getRateMoney())

    def getRate(self):
        return self.__rate

    def setRate(self, rate):
        self.__rate = rate

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if money <= 0:
            raise MinusError

        if self.__balance < money:
            raise ValueError
        self.__balance -= money

    def inquire(self):
        return self.__balance

    def getRateMoney(self):
        m = 0
        m = (self.__balance * self.__rate) / 100
        return m


class MinusError(Exception):
    """ Inappropriate argument value (of correct type). """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass





def getAvg(accList):
    bsum = 0
    rsum = 0

    for acc in accList:
        bsum += acc.balance
        rsum += acc.rate

    return bsum / len(accList), rsum / len(accList)