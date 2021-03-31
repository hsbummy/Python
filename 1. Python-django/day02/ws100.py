gender = "man"
h = 173 * 0.01
w = 65
bmi = round(w / (h*h), 2)

print(bmi)


if bmi > 30 :
    print("fat")
elif 25<= bmi <30:
    print("little fat")
elif 20<= bmi < 25:
    print("good")
else:
    print("skinny")