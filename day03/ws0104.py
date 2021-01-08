# 1. 두 자리의 숫자 2개를 입력 받는다.
# 2. 두 수 사이의 랜덤한 숫자를 발생 시킨다.
# 3. 넘버게임을 시작한다.
# 4. 숫자를 입력 받아 2번에서 만들어진 숫자를 기준으로 3가지의 조건을 출력 한다.
# 5. 게임한 횟수를 화면이 출력 한다.(횟수는 10회)
# 6. 10회가 넘으면 FAIL
# 7. 게임 다시 시작
# 8. 숫자가 맞으면 새로운 게임을 만들어 다시 시작


import random

number = input('두 자리 숫자를 2개 입력하세요...?')
number = number.split(' ')
rn = random.randint(int(number[0]), int(number[1]))
print(rn)
cnt = 10


while True:
    print("game start")

    ans = input("정답은?")
    ans = int(ans)


    if cnt == 0:
        print('FAIL')
        break

    elif rn < ans:
        print("작다")
        cnt -= 1
        print("남은 횟수" + str(cnt))


    elif rn > ans:
        print("크다")
        cnt -= 1
        print("남은 횟수" + str(cnt))


    elif ans == ans:
        print("맞다")
        break


