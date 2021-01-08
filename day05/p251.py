# a=1;
# b=a
#
# print('a:%s b:%s' % (a,b))
#
# a=5
# print('a:%s b:%s' % (a,b))

list1 = [1,2,3,4]
list2 = list1
list3 = list1.copy()
print(list1)
print(list2)

list1[0] = 100
print(list1)
print(list2)
print(list3)


