import sqlite3
import dbutil

print("Start")



try:
    dbutil.connectDB('addr.db')
    dbutil.MakeTable()

    while True:

        menu = input('Input Menu(c,r,ro,u,d,q)')

        if menu == 'q':
            print("ADIOS")
            break

        if menu == 'c':

            sub_menu = input("Input User Data...")
            userdata = sub_menu.split(" ")
            dbutil.insertUser(userdata)


        elif menu == 'r':
            allusers = dbutil.selectUser()
            for u in allusers:
                print('%s %s %s %s %s %d' % \
                      (u[0], u[1], u[2], u[3], u[4], u[5]))


        elif menu == 'ro':
            userid = input("Select User Info... : ")
            oneUser = dbutil.selectOneUser(userid)
            print(oneUser)

        elif menu == 'd':
            DeleteUser = input("Write the name : ")
            dbutil.DeleteUser(DeleteUser)
            print("Delete Complete")


        elif menu == 'u':
            UpdateUser = input("Write the Info : ").split(" ")
            dbutil.UpdateUser(UpdateUser)


except sqlite3.IntegrityError:
    print("Error")

finally:
    dbutil.closeDB()


print("End")





