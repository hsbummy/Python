# f = None
#
# try:
#     f = open('live.txt', "rt", encoding='utf8')
#     text = f.read()
#     print(text)
#
# except:
#     print("file not found")
#
# finally:
#     if f != None:
#         print("close")
#         f.close()
#
a = None

try:
    a = open("texe_2.txt", "rt", encoding="utf8")
    texe_2 = a.read()
    print(texe_2)

except:
    print("file not found")

finally:
    if not a == None:
        print("bye")
        a.close()