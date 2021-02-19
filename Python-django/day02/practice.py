# 데이터의 합과 평균을 구하시오
# A~F 학점을 출력하시오

data = [98, 87, 90, 85, 75, 88]

sum = 0
avg = 0

for x in data:
    sum += x
    avg = round(sum / 6, 2)

print(sum)
print(avg)

if avg > 90:
    print("A")
elif 85 <= avg < 90:
    print("B")
elif 80 <= avg < 85:
    print("C")
elif 75 <= avg < 80:
    print("D")
else:
    print("F")

# 각 학생의 합과 평균을 출력
# 전체 학생의 합과 평균을 출력

data = [[100, 90, 98, 88],
        [100, 90, 98, 87],
        [100, 90, 98, 86],
        [100, 90, 98, 85]
        ]
sum = 0
avg = 0
sumlist = []
avglist = []



for x in range(len(data)):
    for y in data[x]:
        sum += y
        avg = sum / 4
    sumlist.append(sum)
    sum = 0

for z in range(len(sumlist)):
    print("each :", sumlist[z],"avg", sumlist[z]/len(sumlist))

total = 0

for q in sumlist:
    total += q
    print(total)
    print(total/len(sumlist))


