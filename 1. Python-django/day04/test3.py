'''lotto game'''

# 1. 시나리오
# 사용자로부터 6가지 숫자를 입력받는다.
# 당첨금 누적시스템
# 3등까지 당첨금 지급
# 단, 1등 상금은 4개 이상 맞춘 사람만 받을 수 있음
# 금액 범위 (100~10,000)
# 본인 포함 100명의 참가자

# 2. 전제 조건 :
#  - 당첨금은 랜덤하게 만든다.
#  - 당첨 번호는 랜덤하게 만든다.
#  - 순위에 따라 당첨금을 차등 지급한다.
#  - 게임을 끝내고 다시 시작할 수 있다.

import random

def gen_lotto(): # 혹시 이거를 보신다면 설명 좀 부탁드려요
    visited =[0]*46
    ret=[]
    while len(ret) < 6:
        next = random.randint(1,45)
        if visited[next] == 0:
            visited[next] = 1
            ret.append(next)
    return ret

def print_warning():
    print("1~45의 숫자 6개를 다시 입력해주세요")

def get_prize(i, n): # 이 부분도 잘 모르겠어요
    ret = 0
    for idx in range(len(acc_price)):
        if i < 4 and idx ==0:
            continue
        if i < 2 and idx < 2:
            continue
        if acc_price[idx] == 0:
            continue
        ret = acc_price[idx]
        acc_price[idx] = 0
        break
    return int(ret / n)

week = 1
acc_price = [0]* 3
guest = [[] for i in range(100)]

while True:
    price=[]
    for i in range(3):
        price.append(random.randint(100, 10000))
    price.sort(reverse=True)

    for i in range(3):
        acc_price[i] += price[i]

    print('1조의',week,'주차 Lotto Game 현재 상금은', sep='')
    print('1st : %d만원\n2등 : %d만원\n3등 : %d만원' % (acc_price[0],acc_price[1],acc_price[2]))

    score_board ={6:[],5:[],4:[],3:[],2:[],1:[],0:[]}


    lotto = gen_lotto()
    for i in range(99):
        guest[i].clear()
        guest[i] = gen_lotto()

    while True:
        user_num = input("(중복 불가) 숫자 6개 입력 : ")
        if user_num.find(' ') == -1: # 왜 -1 이죠?
            print.warning()
        else:
            user_num = user_num.split(' ')
            while user_num.count('') > 0:
                user_num.remove('')
            if len(user_num) != 6:
                print_warning()
                continue
            guest[99].clear()
            for i in range(len(user_num)):
                if user_num[i].isdecimal() and int(user_num[i]) > 0 and int(user_num[i])<46:
                    guest[99].append(int(user_num[i]))
                else:
                    print_warning()
                    break
            if len(guest[99]) ==6:
                break
    # 스코어 보드 갱신이랑 상금분배 부분이 이해가 잘 안되는데 혹시 설명 좀 해주실 수 있나요?
    for idx in range(100):
        cnt =0
        for n in guest[idx]:
            if n in lotto:
                cnt += 1
        score_board[cnt].append(idx+1)

    for i in range(6, 0 ,-1):
        if len(score_board[i]) != 0:
            money = get_prize(i, len(score_board[i]))
            if money ==0:
                break

            print('winner')
            print(score_board[i])
            print('상금', money, "만원을 획득하셨습니다.")

    print('다음 주에 만나요')
