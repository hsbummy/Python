# for n in range(1, 100, 5):
#     print(n)
#
list = [];
for n in range(1, 100, 5):
    list.append(n)

print(list)


for n in range(1, 51):
    if n % 10 == 0 :
        print("+", end='')
    else:
        print("-", end='')

for n in range(1,11):
    print(n);
    if n == 7:
        break;

for n in range(1,11):
    if n % 2 == 0:
        continue
    print(n)