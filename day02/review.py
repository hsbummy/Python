# data = [1,2,3,4,5];
#
# print(data);
# sum = 0
# for x in data:
#     sum += x
#
#
# print(sum)

datas= [\
    [1,2,3,4],\
    [5,6,7,8],\
    [9,10,11,12],\
    ]
# print(datas)

for x1 in datas:
    for x2 in x1:
        print(x2,end='')
    print(x1)