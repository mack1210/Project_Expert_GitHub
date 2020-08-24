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

'''
# #Quiz 1
# station = ["사당", "신도림", "인천공항"]
# for i in station:
#     print(i, "행 열차가 들어오고 있습니다.")
'''

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
# from random import *
# for i in range(0,2):
#     x[i] = randint(4, 28)
#     print("오프라인 스터디 모임 날짜는 매월 ", x[i], "일로 선정되었습니다.")

# #문자열
# sentence = """
#     나는 소년이고
#     파이썬은 쉬워요.
#     """
# print(sentence)

# #슬라이싱
# jumin = "991231 - 1234567"
# print("성별 : " + jumin[9])
# print("연 : " + jumin[0:2]) #실제 자릿 수 보다 하나 더 입력해야함
# print("생년월일 : " + jumin[:6])
# print("뒷 일곱자리 : " + jumin[9:])
# print("뒷 일곱자리 : " + jumin[-7:]) #뒤에서 부터 계산했을 경우

#문자열 처리함수
# python = "Python is amazing!"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "JAVA"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1) #index+1 은 시작위치를 나타냄
# print(index)

# print(python.find("n"))
# print(python.find("Java"))
# print(python.index("Java"))
# print(python.count("n"))

# #문자열 포멧
# print("a", "b")

# # 1)
# print("나는 %d살 입니다." % 20)
# print("나는 %s을 좋아합니다." % "파이썬")
# print("Apple이란 단어는 %c로 시작해요." % 'A')

# print("나는 %s살 입니다." % 20) #oh
# print("나는 %s와 %s를 좋아합니다." % ("파이썬", "Jave"))

# # 2)
# print("나는 {}살 입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨강"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨강"))

# # 3)
# print("나는 {age}살이며 {color}색을 좋아해요.".format(age = 20, color = "빨강"))

# # 4) v3.6이상
# age = 20
# color = "빨강"

# print(f"나는 {age}살이며, {color}색을 좋아해요.")



####### 탈출문자
# # \" 혹은 \' 은 문장 내에서 따옴표로 사용할 수 있다.
# print("백문이 불여일견\n 백견이 불여일타")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")

# #\\ : 문장 내에서 \
# print("C:\\Python\\Python38")
# print("C:/Python/Python38")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")
# print("Red Apple\rPineTree")

# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# #\t : tab
# print("Red\tApple")

'''
# Quiz 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1 : http:// 부분 제외
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
# 예) 생성된 비밀번호 : nav51!
# url = "http://naver.com"
# url = "http://google.com"
# url = "http://youtube.com"
# my_str = url.replace("http://", "") # 규칙1
# my_str = my_str[:my_str.index(".")] # 규칙2
# passward = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1} 입니다.".format(url, passward))
'''


# ###### 리스트
# subway = [10, 20, 30]

# subway = ["유재석", "조세호", "박명수"]
# #조세호씨가 몇 번째 칸에 타고 있는가.
# print(subway.index("조세호")+1)
# #하하가 탄다
# subway.append("하하")
# #정형돈을 유재석, 조세호 사이
# subway.insert(1, "정형돈")
# #한명씩 뒤에서 꺼낸다.
# subway.pop()
# #같은 이름의 사람이 몇 명 있는가
# subway.append("유재석")
# subway.count("유재석")

# #정렬
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)
# num_list.reverse()
# print(num_list)
# #모두지우기
# num_list.clear()

# #다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]
# print(mix_list)

# #list 확장
# num_list.extend(mix_list)
# print(num_list)



####### 사전
# cabinet = {3: "유재석", 100: "김태호"} #key는 3, data는 유재석
# print(cabinet[100])
# print(cabinet.get(3))
# #특징!
# print(cabinet[1])   #여기서 종료돼서 밑에 hi가 출력이 안됨
# print("Hi")
#                     #반면
# print(cabinet.get(1))
# print("Hi") #여기서 종료

# print(cabinet.get(1, "not occupied")) #default value is "not occupied"

# #존재여부 확인
# print(3 in cabinet)
# print(5 in cabinet)

# #응용
# cabinet = {"A-3": "유재석", "B-100": "김태호"}
# print(cabinet["B-100"])

# #새 손님
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"

# #손님 퇴장
# del cabinet["A-3"]
# print(cabinet)

# #key들만 출력
# print(cabinet.keys())
# #value들만 출력
# print(cabinet.values())
# #key, values 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 페점
# cabinet.clear()
# print(cabinet)

# ##### 튜플 리스트보다 빠름
# menu = ("돈까스", "치즈까스")
# print(menu)
# # menu.add("생선까쓰") # 튜플은 고정된 메뉴에만 사용가능, 이렇게 추가할 수 없다.

# # 1)
# name = "김종국"
# age = 20
# hobby = "코딩"

# # 2)
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)



# ####### 세트
# #중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# Java = {"유재석", "김태호", "양세형"}
# print(Java)
# python = set(["유재석", "박명수"])
# print(python)

# #교집합 (java와 python을 모두 할 수 있는 개발자)
# print(Java & python)
# print(Java.intersection(python))

# #합집합 (java와 python을 모두 할 수 있는 개발자)
# print(Java | python)
# print(Java.union(python))

# #차집합 (java가능, python 불가능)
# print(Java - python)
# print(Java.difference(python))

# #python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # Java를 까먹음
# python.remove("김태호")
# print(Java)


########### 자료구조의 변경
# #커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

'''Quiz
참석률 높이기위해 댓글 작성자 들 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 준다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

(활용 예제)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))
'''
# from random import *
# lst = list(range(1, 21, 1)) #조건1
# winners = sample(lst, 4)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")


###### IF
# if 조건:
#     실행 명령문
# weather = input("청주 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("Good!")
# elif 0 <=temp < 10:
#     print("외투!!")
# else:
#     print("너무 추워요!")


##### for loop
# for Waiting_no in range(1,21):
#     print("대기번호: {0}".format(Waiting_no))

# starbucks = ["아이언맨", "토르", "베트맨"]
# for customer in starbucks:
#     print("{0}, 커피 완료!".format(customer))

###### while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 더 부르고 버리겠습니다.".format(customer, index))
#     index -= 1
#     if index ==0:
#         print("커피는 폐기 처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}번째".format(customer, index))
#     index += 1

customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))