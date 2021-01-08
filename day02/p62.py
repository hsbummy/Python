# 1. 수치형 2. 문자형

a = 100
b = 1.2222222
c = 12222e2

aa = 0xff # 16진수 - 비트를 많이 사용하기 위해서 FF = 255
bb = 0o77 # 8진수
cc = 0b1101 # 2 진수

aaa = 255
bbb = 63
ccc = 131313131313


#16진법 접두 : 0x # 꼭 안 붙어도 된다
#8진법  접두 : 0o
#2진법  접두 : 0b
print(a,b,c,(a+b), sep=",")
print(aa, bb, cc)
print(hex(aaa),oct(bbb),bin(ccc), sep=",")

