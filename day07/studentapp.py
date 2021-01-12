import studentapi
from studentapi import Human, Student

human = Human('james', 25)

print("이름 : %s , 나이 %s " % (human.print()))

st = Student("kim",25,"En")


print("이름 : %s | 나이 %s | 전공 %s " % (st.print()))
print(st.study())