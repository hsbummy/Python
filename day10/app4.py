str = "3+4+5"

strlist = "[1,2,3,4,5]"

print(eval(str))
print(strlist)

for i in eval(strlist):
    print(i)

users = """[
{'id':'id01','name':'james'},
{'id':'id02','name':'james'},
{'id':'id03','name':'james'}
]"""

for u in eval(users):
    print(u['id']+u['name'])



us = """[
{'id':'id01','name':'james'},
{'id':'id02','name':'james'},
{'id':'id03','name':'james'}
]"""


usstr = repr(us);
print(usstr)