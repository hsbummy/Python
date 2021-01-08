# CART 구현

# 1. 상품이름, 가격, 개수
# 2. 위의 항목을 입력 받아서 CART에 넣는다.

# [['item1',1000,1],['item2', 2000,1],['itme3',3000,1]]

#1.메뉴 카트에 넣기 2. 카트 정보 보기



print('start')


list = []

while True:

    menu = input('Input Menu(i,v,q)')
    if menu == 'i':
        CART = input('Input Item(name,price,count)')
        CART = CART.split(' ')
        list.append(CART)


    if menu == 'v':
        print('view')
        ptotal = 0
        ctotal = 0
        for CART in list:
            print(('name: %s' 'price: %d' 'count: %d' ) % (CART[0], int(CART[1]), int(CART[2])))
            ptotal += int(CART[1])
            ctotal += int(CART[2])
            print('%d %d' % (ptotal, ctotal))


    if menu == 'q':
        print('ADIOS')
        break



print('end')