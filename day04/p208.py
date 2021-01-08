#
#
# print('start')
#
# cart = []
#
# def viewCart(c):
#     print('view')
#     ptotal = 0
#     ctotal = 0
#     for item in cart:
#         print('Item: %s %d %d' % (item[0], int(item[1]), int(item[2])))
#         ptotal += int(item[1])
#         ctotal += int(item[2])
#     print('total: %d %d' % (ptotal, ctotal))
#
# while True:
#
#     menu = input('Input menu(i,v,q)')
#     if menu == 'i':
#         item = input('Input Item(name,price,count)')
#         item = item.split(' ')
#         cart.append(item)
#     if menu == 'v':
#         viewCart(cart)
#
#     if menu == 'q':
#         print('ADIOS')
#         break
#
#
# print('End')




print('start')

cart = []

def viewCart(c):
    print('view')
    ptotal = 0
    ctotal = 0
    for item in cart:
        print('Item: %s %d %d' % (item[0], int(item[1]), int(item[2])))
        ptotal += int(item[1])
        ctotal += int(item[2])
    print('total: %d %d' % (ptotal, ctotal))

while True:

    menu = input('Input menu(i,v,q,r)')
    if menu == 'i':
        item = input('Input Item(name,price,count)')
        item = item.split(' ')
        cart.append(item)
    if menu == 'v':
        viewCart(cart)

    if menu == 'r':
        itemname =input('Input Name...?')
        for c_item in cart:
            if itemname in c_item:
                cart.remove(c_item)
                print(c_item[0] + '삭제 되었습니다.')


    if menu == 'q':
        print('ADIOS')
        break


print('End')