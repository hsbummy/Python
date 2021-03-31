# print("Start")
#
# a = input("Input number..?")
# if int(a) > 10:
#     print("Big number")
# elif int(a) > 5 :
#     print("Middle number")
# elif int(a) > 1:
#     print("Small number")
# else :
#     print("nothing")
# print("End")

# print("Start")
#
# a = input("Input number..?")
# if int(a) % 2 == 0 :
#     print("good")
# else:
#     print("bad")
#
#
# print("End")

#
print("Start")

ko = input("input ko score")
en = input("input en score")
si = input("input si score")
ma = input("input ma score")

avg = (int(ko) + int(en) + int(si) + int(ma)) / 4
print(avg)

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

print("End")


num = 15;

if num > 5 and num < 20:
    print("ok")

if 5 < num < 20:
    print
