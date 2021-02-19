import dbutil

print('start!')

while True:
    menu = input('Input menu...[i,s,sa,q]')
    if menu.lower() == 'q':
        print('BYE')
        break
    if menu.lower() == 'i':
        datas = input('Input information...[id,pwd,name,age]')
        datas = datas.split(' ');
        dbutil.insert(id=datas[0].strip(),pwd=datas[1].strip(),name=datas[2].strip(),age=int(datas[3].strip()));

    if menu.lower() == 'sa':
        users = dbutil.allselect();
        for user in users:
            print('user info: %s %s %s %d' % (user[0], user[1], user[2], user[3]))


    if menu.lower() == 's':
        inputid = input('input user id')
        user = dbutil.select(id=inputid)
        print('user info: %s %s %s %d' % (user[0], user[1], user[2], user[3]))



print('end')
