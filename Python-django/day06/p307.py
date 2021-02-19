# f= None
#
# try:
#     f = open("live.txt", "rt", encoding='utf8')
#     while True:
#         text = f.readline()
#         if not text:
#             break
#         print(text)
#         for text in f:
#           print(text, end='')
#
# except:
#     print("error")
#
# finally:
#     if not f == None:
#         f.close()
#
# print("end")

f = None
try:
    f = open("texe_2.txt","rt",encoding="utf8")
    while True:
        text = f.readline()
        if not text:
            break
        print(text)


except:
    print("error")

finally:
    if not f == None:
        f.close()