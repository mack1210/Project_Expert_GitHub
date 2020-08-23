#참과 거짓
# print(not True)
# print(not(5>10))

#애완동물을 소개해 주세요
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 5

#1 with +
# print("우리집 " + animal + "의 이름은 "+ name)
# print(name + "는 " + str(age) + "살이며, "+ hobby +"을 아주 좋아해요")
# print("연탄이는 어른일까요? "+ str(is_adult))

# #2 with ,
# print("우리집 ", animal, "의 이름은 ", name)
# print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
# print("연탄이는 어른일까요? ", str(is_adult))

# #Quiz 1
# station = ["사당", "신도림", "인천공항"]
# for i in station:
#     print(i, "행 열차가 들어오고 있습니다.")

# #연산자   
# print(abs(-5))
# print(pow(4,2))

# from math import *
# print(floor(4.99))
# print(ceil(3.14))
# print(sqrt(16))

# #Random function
from random import *
# print(random())
# print(random()*10)
# print(int(random() * 10))
# print(int(random() * 10 + 1))
# print(int(random() * 45 + 1))
# print(int(random() * 45 + 1))
# print(int(random() * 45 + 1))
# print(int(random() * 45 + 1))
# print(int(random() * 45 + 1))
# print(int(random() * 45 + 1))

# print(randrange(1, 46))
# print(randint(1,46))


'''
Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.

condition
1) 랜덤으로 날짜 뽑기
2) 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
3) 매월 1~3일은 스터디 준비를 해야하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 X 일로 선정되었습니다.
'''
from random import *
for i in range(0,2):
    x[i] = randint(4, 28)
    print("오프라인 스터디 모임 날짜는 매월 ", x[i], "일로 선정되었습니다.")

#문자열
sentence = """
    나는 소년이고
    파이썬은 쉬워요.
    """
print(sentence)

#슬라이싱
jumin = "991231 - 1234567"
print("성별 : " + jumin[9])
print("연 : " + jumin[0:2]) #실제 자릿 수 보다 하나 더 입력해야함


