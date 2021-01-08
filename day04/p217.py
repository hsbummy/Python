import random
score = (10,20,30,40)

print(type(score))

print(score[0])
print(score[0:2])

score = score + (50,60,70)
print(score)

scorelist = list(score)
print(type(scorelist))
print(scorelist)

# t = ()
t=[]
for i in range(1,7):
    temp = random.randint(1,45);
    # temp = random.randint(1,3) = 중복가능
    # 그냥 int 값을 넣을 수는 없다. 튜플에는
    t.append(temp)
#
print(t)

tp = tuple(t)
print(type(tp))