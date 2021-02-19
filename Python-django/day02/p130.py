# for n in range(2, 10):
#     if n % 2 == 1:
#         continue
#     print(str(n)+"단")
#     for m in range(1,10):
#         print(n, m, (n*m), sep= "-")


# for n in range(2,10):
#     if n % 2 ==1:
#         continue
#     if n == 6:
#         print(str(n)+"단")
#     for m in range(1,10):
#         if n == 6 and m == 5 :
#             break
#         print(n, m, (n*m))
#
# for n in range(2,10):
#     if n > 6:
#         break
#     if n % 2 == 1
#         continue
#     print(str(n) + "단")
#     for m in range(1, 10):
#         print(n, m, (n*m), sep= "-")

# for n in range(2, 10):
#     print(str(n)+"단")
#     for m in range(1, 10):
#         print(n, m, (n*m), sep="")

for x in range(2,10):
    print(str(x) + "단")
    for y in range(1, 10):
        print(x, y, (x*y), sep="!")

for x in range(2, 10):
    print(str(x) + "단")
    if x > 6:
        break
    for y in range(1, 10):
        if y > 6:
            break
        print(x, y ,(x*y))