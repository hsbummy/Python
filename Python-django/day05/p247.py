# score = [90,80,60,100];
#
#
# def my_filter(n):
#     return n >=90;



# for i in filter(my_filter, score):
#     print(i)


# for i in filter(lambda x:x>=90, score):
#     print(i)
score= [77,88,99,66,55]

def my_filter(n):
    return n >=85

for i in filter(my_filter, score):
    print(i)

for i in filter(lambda x:x>=85, score):
    print(i)