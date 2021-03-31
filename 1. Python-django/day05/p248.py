# score = [93,87,65,100];
#
#
# def my_map(n):
#     return n / 3;

# for i in map(my_map,score):
#     print(i)


# for i in map(lambda x:x/3,score):
#     print(i)

score = [81,93,45,21]

def my_map(n):
    return n /3

for i in map(my_map,score):
    print(i)

for i in map(lambda x:x/3, score):
    print(i)