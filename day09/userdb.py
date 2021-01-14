from sqlitedb import *
from value import User


class UserDb(SqliteDb):

    def __init__(self, dbname):
        super().__init__(dbname)

    def insert(self, u):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.insertUser % u.sqlmap())
        cc['con'].commit()
        self.close(cc)


    def select(self):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.selectAllUser)
        result = cc['cursor'].fetchall()
        all = []
        for u in result:
            tu = User(u[0], u[1], u[2], u[3])
            all.append(tu)
        self.close(cc)
        return all


    def selectone(self, id):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.selecUser % (id))
        obj = cc['cursor'].fetchone()
        result = User(obj[0], obj[1], obj[2], obj[3])
        self.close(cc)
        return result


    def delete(self, id):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.deleteUser % (id))
        cc['con'].commit()
        self.close(cc)

    def update(self, u):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.updateUser % (u.pwd, u.name, u.age, u.id))
        cc['con'].commit()
        self.close(cc)
