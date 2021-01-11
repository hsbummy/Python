import sqlite3

con = None
cursor = None

def connectDB(dbName):
    "Connect SQLite"
    global con, cursor
    con = sqlite3.connect(dbName)
    cursor = con.cursor()

def MakeTable():
    "Make users Table"
    # p320 테이블 만드는 부분

def insertUser(user):
    "Insert User Data"
    insertSQL = "INSERT INTO users VALUES ('"+user[0]+"','"+user[1]+"','"+user[2]+"','"+user[3]+"','"+user[4]+"',"+str(user[5])+")"
    # """INSERT INTO %s VALUES('%s','%s','%s','%s','%s','%d')""" % (db, user['id'],user['pwd'],user['이름'],user['번호'],user['주소'],user['나이'])
    cursor.execute(insertSQL)
    con.commit()

def selectUser():
    "Select User Data"
    allusers = []
    selectSQL = """SELECT * FROM users"""
    users = cursor.execute(selectSQL)
    for u in users:
        user = []
        user.append(u[0])
        user.append(u[1])
        user.append(u[2])
        user.append(u[3])
        user.append(u[4])
        user.append(u[5])
        allusers.append(user)
    return allusers

def selectOneUser(id):
    "Select One User"
    user = []
    selectOneSQL = """SELECT * FROM users WHERE id='%s'""" % (id)
    cursor.execute(selectOneSQL)
    userData = cursor.fetchone()
    user.append(userData[0])
    user.append(userData[1])
    user.append(userData[2])
    user.append(userData[3])
    user.append(userData[4])
    user.append(userData[5])
    return user

def DeleteUser(id):
    "Delete One User"
    deleteSQL = """DELETE FROM users WHERE id='%s'""" % (id)
    cursor.execute(deleteSQL)
    con.commit()

def UpdateUser(user):
    "Update One User"
    updateSQL = """UPDATE users SET pwd='%s',name='%s',phone='%s',addr='%s',age='%d' WHERE id='%s'""" % \
                (user[1],user[2],user[3],user[4],user[5],user[0])
    cursor.execute(updateSQL)
    con.commit()



def closeDB():
    "Close SQLite"
    if not cursor == None:
        cursor.close()
    if not con == None:
        con.close()