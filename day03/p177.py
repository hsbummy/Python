s = 'python programming';

# print(type(s));
# print(type(s[0]));
#
# print(s.find("o"))
# print(s.rfind("o"))
# print(s.index("r"))
# print(s.rindex("r"))
# print(s.count('o'))

# 두 개가 있을 때 뒤에것 찾을 때 = r

# print('a' in s)
# print('a' not in s)
#
#
# if('a' in s) == True:
#     print("OK")
# else:
#     print("NO")
#
# if s.startswith('p') == True:
#     print('ok1')
#
# if s.endswith('g') == True:
#     print('OK2')

a = 'computer program'
print(a.find("c"))
print(a.rfind("o"))
print(a.index('a'))
print(a.rindex('m'))

print('w' not in a)

if a.endswith('m'):
    print("ok")

if a.startswith('c'):
    print("ok2")