
# 1. 사용하고자 하는 데이터베이스 이름을 이용한다.
from itemdb import ItemDb
from userdb import *
from value import Item

sqlitedb = SqliteDb('shopdb.db')


# 2. 테이블을 생성 한다. 단, 존재 하지않으면

sqlitedb.makeTable()


# 3. 사용자 테이블을 사용하기 위해 userdb 객체를 이용하여 CRUD 진행
udb = UserDb('shopdb.db')
user = User('id05','pwd05','james',20)
# udb.insert(user)

userlist = udb.select()
for u in userlist:
    print(u)


# idb = ItemDb('shopdb.db')
# item = Item('it04','pants', 10000)
# idb.insert(item)
#
# itemlist = idb.select()
# for it in itemlist:
#     print(it)

def userInsert(user):
    userdb = UserDb("shopdb.db")
    userdb.insert(user)

def init():
    userdb = UserDb("shopdb.db")
    return userdb.select()