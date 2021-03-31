from humanapi import Human

human = Human('id01','james', 3000)
# human.setSalary(4000)
# human.salary = 19999999

# print(human.getSalary())
# print(human.getName())
# print(human.getId())
#
# human.sal = 4000
# print(human.sal)

human.setSalary(4000)
human._Human__salary=100000
print(human.getSalary())