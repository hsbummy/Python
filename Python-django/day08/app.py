from sqlitedb import *
from value import *

print('start')

Sql = SqliteDb('udb.db')
Sql.makeTable()
u = user('id02','pwd02','james',28)
Sql.insert()
UserList = Sql.select()
for us in UserList:
    print(us.id + " " + us.name+ " " + str(us.age))
print()
userone = Sql.selectone('id01')
print(userone)



print('end')









