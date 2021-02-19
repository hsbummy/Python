# score = []
# score1 = [10,20,30,40,50,60,70,80]
# score2 = [[10,20,30,40],[10,20,30,40]]
# print(score1[1:3])
# temp =score1[1:5:2]
# print(temp)
#
# sum = 0
# for i in score1:
#     sum += i
#     print(i)
# print('Result : %d %10.2f' % (sum, sum/len(score1)))

#

score2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]


total = 0
total_cnt = 0
for i in score2:
    sum =0
    cnt = len(i)
    for i1 in i:
        print(i1)
        sum += i1
    print('%d %.2f' % (sum, sum/cnt))

    total += sum
    total_cnt += cnt
print('%d %.2f' % (total, total/total_cnt))







# print(score2[1][3])
# total = 0
# total_cnt = 0
# for i in score2:
#     sum=0
#     cnt=len(i)
#     print(i)
#     for i1 in i:
#         sum += i1
#     print('%d %.2f' % (sum, sum/cnt))
#     total += sum
#     total_cnt += cnt
# print('%d %.2f' % (total, total/total_cnt))
#
# sum_list= []
#
# for i in score2[0]:
#     sum_1 =0
#     sum_1 += i
#     avg = sum_1 / len(score2[0])
#
#     sum_list.append(sum_1)
#
# print(sum_list)
#


