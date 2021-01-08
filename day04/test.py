# CART 구현

# 1. 상품이름, 가격, 개수
# 2. 위의 항목을 입력 받아서 CART에 넣는다.

# [['item1',1000,1],['item2', 2000,1],['itme3',3000,1]]

#1.메뉴 카트에 넣기 2. 카트 정보 보기

print('start')

list = []

while True:
    menu = input('input keyword (i,v,q)')
    if menu == 'i':
        cart = input('input items(name, price, count')
        cart = cart.split(' ')
        list.append(cart)

    if menu == 'v':
        ptotal=0
        ctotal=0
        for cart in list:
            print('%s : name, %d : price, %d : count' % (cart[0],int(cart[1]),int(cart[2])))
            ptotal += int(cart[1])
            ctotal += int(cart[2])
            print('%d : price %d : count' % (ptotal,ctotal))
    if menu == 'q':
        print('Bye')
        break



print("end")