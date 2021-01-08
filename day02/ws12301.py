# 데이터의 합과 평균을 구하시오
# A~F 학점을 출력하시오

data = [98, 87, 90, 34, 56, 43]
sum = 0
avg = 0

for n in data:
    sum += n

avg = sum / 6

if avg >= 90:
    print("A")
elif avg < 90 and avg >=80:
    print("B")
elif avg <80 and avg >= 70:
    print("C")
elif avg <70 and avg >=60:
    print("D")
else:
    print("F")

print(sum)
print(avg)

# 각 학생의 합과 평균을 출력
# 전체 학생의 합과 평균을 출력

data = [[100, 90, 98, 88],
        [100, 90, 98, 87],
        [100, 90, 98, 86],
        [100, 90, 98, 85]
        ]
sum = 0
avg = 0
sum_list = []
avg_list = []
for x in range(len(data)):
    for y in data[x]:
        sum += y;
        avg = sum /4;
    sum_list.append(sum)
    sum = 0
for z in range(len(sum_list)):
    print("each sum=",sum_list[z], "each avg=", sum_list[z]/len(sum_list))

totalsum =0

for a in sum_list :
    totalsum += a
    print("total=",totalsum,"totalavg=",totalsum/len(data))









# 10진수를 16진수 , 8진수, 2진수로 변경 하는 과정 및 그 반대에 대한 처리 방법 정리





# data = [[100, 90, 98, 88],
#         [100, 90, 98, 87],
#         [100, 90, 98, 86],
#         [100, 90, 98, 85]
#         ]
#
# total_score = 0
# student = [0,0,0,0]
#
# for i in range(len(data)):
#     for j in range(len(data)):
#         student[i] += data[i][j]
#         total_score += data[i][j]
#
# for i in range(len(student)):
#     print("각 학생의 값 : {0}, 학생의 평균: {1} :".format(student[i], student[i]/len(student)))
#
# print("전체 학생의 합: {0}, 평균 : {1}".format(total_score, total_score/4))
