s = [];
s.append(20)
s.append(30)
s.append(10)
s.append(70)
s.append(50)
s.insert(2,99)
s[3]= [1,2,3]
del(s[0])
s.remove(50)
print(s)
del s[3]
print(s)
s[1:3] = [1,2,3]
print(s)
s = s+ [9,8,7]
print(s)
s.sort(reverse=True)
print(s)
# print(s.pop(0))
# print(s)
# print(s.pop(1))
print(s.index(30))
# s.append(30)
print(s.count(30))
print(s)


str =['A','B','C','D','D']
#
# if 'A' in str:
#     print('OK')
#
# else:
#     print('No')

if 'A' in str:
    str.remove('A')
    print(str)
else:
    str.append('A')
