import sqlite3

import dbutil

try:
    #SQLite 에 접속한다.

    dbutil.connectDB('addr.db')

    #Table 을 만든다.

    dbutil.MakeTable()

    #사용자 정보를 입력 한다.

    user = ['id09','pwd0','엄복동','01013245678','경기',20]
    # dbutil.insertUser(user)

    # 3-1. 한 명 조회

    oneUser = dbutil.selectOneUser('id09')
    print(oneUser)

    # 3-2. 수정
    user = ['id09','pwd09','엄복동','01013245678','경기',20]
    dbutil.UpdateUser(user)

    # 3-3. 삭제

    dbutil.DeleteUser('id02')

    #사용자 정보를 조회 한다.

    allusers = dbutil.selectUser()
    for u in allusers:
        print('%s %s %s %s %s %d' % (u[0],u[1],u[2],u[3],u[4],u[5]))

except sqlite3.IntegrityError:
    print("")

#SQLite를 close 한다.
finally:
    dbutil.closeDB()