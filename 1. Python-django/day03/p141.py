import p140;

# p140.data = 200

data = [1,2,3,4,5]
result= p140.calcsum(data)

print(result)

result1 = p140.f1();
print(result1)

result2 =  p140.f2(2,9);
print(str(result2) + "평균")
# 리턴값이 굳이 필요는 없지만 함수에는 출력 구문 ㄴㄴ

p140.f3(4, 9);

result4 = p140.f4(1,2,3,4,5,6)
print(result4)

result5 = p140.f5(100, 1,2,3,4,5,6)
print(result5)

result6 = p140.f6(step=2, end=100, begin=1)
print(result6)

# help(p140.f6)
#
# result7 = p140.f7(s=2, e=100, b=1)
# print(result7)
#
#
# p140.f8('datas',1,2,3,4,5,start=10, end=10)
#
