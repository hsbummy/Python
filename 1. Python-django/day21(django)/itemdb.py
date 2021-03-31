from frame.db import Db
from frame.sql import Sql
from frame.value import Item

class ItemDb(Db):
    def insert(self, name, price, imgname):
        try:
            conn = super().getConnection();
            cursor = conn.cursor()
            cursor.execute(Sql.iteminsert % (name, price, imgname));
            conn.commit()
            
        except:
            conn.rollback()
            raise Exception
        finally:
            super().close(conn, cursor)

    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor()
        cursor.execute(Sql.itemlist)
        result = cursor.fetchall()
        all = [];
        for i in result:
            item = Item(i[0],i[1],i[2], i[3],i[4])
            all. append(item)
        super().close(conn,cursor)
        return all

    def selectone(self,id):
        conn = super().getConnection();
        cursor = conn.cursor()
        cursor.execute(Sql.itemlistone % id)
        i = cursor.fetchone();
        item = Item(i[0],i[1],i[2],i[3],i[4])
        super().close(conn, cursor)
        return item


    def update(self,id, name, price, imgname):
        try:
            conn = super().getConnection();
            cursor = conn.cursor()
            cursor.execute(Sql.itemupdate % (name, price, imgname, id));
            conn.commit()
            
        except:
            conn.rollback()
            raise Exception
        finally:
            super().close(conn, cursor)



    def delete(self,id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor()
            cursor.execute(Sql.itemdelete % (id));
            conn.commit()
            
        except:
            conn.rollback()
            raise Exception
        finally:
            super().close(conn, cursor)



def iteminsert_test():
    ItemDb().insert('shirts',30000,'s.jpg')

def itemlist_test():
    items = ItemDb().select();
    for i in items:
        print(i)

def itemlistone_test():
    items = ItemDb().selectone('id01')
    print(items);

if __name__ == '__main__':
    iteminsert_test();

    