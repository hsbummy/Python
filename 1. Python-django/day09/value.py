class User:
    def __init__(self, id, pwd, name, age):
        self.__id = id
        self.__pwd = pwd
        self.__name = name
        self.__age = age

    def __str__(self):
        return self.__id+" "+self.__pwd + " " + self.__name + " " +str(self.__age)+ " "


    def sqlmap(self):
        return self.__id , self.__pwd, self.__name , self.__age

    def getid(self):
        return self.__id

    def setid(self , id):
        self.__id = id

    def getpwd(self):
        return self.__pwd

    def setpwd(self, pwd):
        self.__pwd = pwd

    def getname(self):
        return self.__name

    def setname(self, name):
        self.__name = name

    def getage(self):
        return self.__age

    def setage(self, age):
        self.__age = age

    id = property(getid, setid)
    pwd = property(getpwd, setpwd)
    name = property(getname, setname)
    age = property(getage, setage)


class Item:
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    def __str__(self):
        return self.__id+" " + self.__name + " " +str(self.__price)+ " "


    def sqlmap(self):
        return self.__id , self.__name , self.__price

    def getid(self):
        return self.__id

    def setid(self , id):
        self.__id = id

    def getname(self):
        return self.__name

    def setname(self, name):
        self.__name = name

    def getprice(self):
        return self.__price

    def setprice(self, price):
        self.__price = price

    id = property(getid, setid)
    name = property(getname, setname)
    age = property(getprice, setprice)