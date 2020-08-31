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
# from random import *
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

# #문자열 처리함수
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

# customer = "토르"
# person = "Unknown"
# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?") 



# # continue와 break
# absent = [2, 5] #결석
# no_book = [7] #책 깜빡
# for student in range(1, 11): #1부터 10번까지 책 읽힐 것
#     if student in absent:
#         continue # 반복문 탈출 실패 countinue는 밑의 내용으로 진행하지 않고 다시 for문으로 올라가서 진행
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student)) #엄한 선생님이라서 수업을 바로 끝내버림
#         break #반복문 탈출
#     print("{0}, 책을 읽어봐!".format(student))

# # 한줄 for loop
# # 출석번호가 1 2 3 4 앞에 100을 붙이기로 함. 101, 102, 103, 104 ...
# students = range(1,6)
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환
# students = ["Iron", "Thor", "Groot"]
# students = [len(i) for i in students]
# print(students)

# # 학생 이름들을 대문자로 변환
# students = ["Iron", "Thor", "Groot"]
# students = [i.upper for i in students]
# print(students)

'''
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건 1: 승객별 운행 소요 시간은 5~50 사이의 난수로 정해집니다.
조건 2: 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[0] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)
'''
# from random import randint
# total = 0
# for i in range(1,51):
#     t = randint(5,51) #5부터 50분 사이의 시간
#     if 5 <= t <= 15:   
#         print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(0, i, t))
#         total += 1
#     else:
#         print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(" ", i, t))
# print("\n총 탑승 승객 : {}분".format(total))


# ######### 함수
# def open_accoun():
#     print("새로운 계좌가 생성되었습니다.")

# open_accoun()

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance+money

# deposit(100, 200)

# def withdraw(balance, money):
#     if(balance >= money):
#         print("출금 완료. 잔액은 {0}원 입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("출금 불가. 잔액은 {0}원 입니다.".format(balance))

# withdraw(200, 100)

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance -money -commission #tuple형식으로 보낸다
# balance = 0
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t 주 사용 언어 : {2}"\
#         .format(name, age, main_lang)) # \ 를 붙이면 두 문장을 한 문장으로 여김
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업. 기본 값을 넣어보자
# def profile(name, age = 17, main_lang = "파이썬"):
#     print("이름 : {0}\t나이 : {1}\t 주 사용 언어 : {2}"\
#         .format(name, age, main_lang)) # \ 를 붙이면 두 문장을 한 문장으로 여김

# profile("유재석")
# profile("김태호")

#키워드 값
# def profile(name, age, main_lang):
#     print(name, age, main_lang) # \ 를 붙이면 두 문장을 한 문장으로 여김
# profile(name = "유재석", age = 20, main_lang = "파이썬")
# profile(main_lang = "자바", age = 25, name = "김태호")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") #end가 붙으면 옆으로 출력, 없으면 밑으로 출력이 된다.
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "파이썬", "자바", "C", "C++", "C#")
# profile("김태호", 20, "코틀린", "스위프트", "", "", "")

# #### 가변인자 (위에가 불편)
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") #end가 붙으면 옆으로 출력, 없으면 밑으로 출력이 된다.
#     for lang in language:
#         print(lang, end = " ")
#     print()

# profile("유재석", 20, "파이썬", "자바", "C", "C++", "C#")
# profile("김태호", 20, "코틀린", "스위프트")


# ############### 지역 변수와 전역 변수
# gun = 10
# def checkpoint(soldiers): #경계근무
#     global gun #전역공간에 있는 gun사용 #메모리를 많이 먹기에 권장되는 방법은 아님 
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2) # 2명이 경계 근무 나감
# gun = checkpoint_ret(gun, 4)
# print("남은 총 : {0}".format(gun))

'''Quiz) 표준 체중을 구하는 프로그램을 작성하시오.
    키(m), 몸무게kg
    남: 키 * 키 * 22
    녀: 키 * 키 * 21

    조건1) 표준 체중은 별도의 함수 내에서 계산
            * 함수명 : std_weight
            * 전달값 : 키(height), 성별(gender)
    조건2) 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''
# def std_weight(height, gender):
#     if gender == "남":
#         return height**2 * 22
#     elif gender == "녀":
#         return height**2 * 21

# height = 175 #cm 단위
# gender = "남"
# weight = round(std_weight(height/100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))


# ######### 표준입출력
# print("python", "Java", "JavaScript", sep = ", ", end = "?") #end : change the last word of the sentence as the word set in the 'end' variable
# print("무엇이 더 재밌을까요?")

# import sys
# print("python", "Java", "JavaScript", file = sys.stdout)
# print("python", "Java", "JavaScript", file = sys.stderr)

# #시험 성적 사전 (key, value)
# scores = {"수학":0, "영어":50, "코딩":100}

# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep = ":") # ljust : left adjust and make space for 8 letters

# #은행 대기 순번표
# #001, 002, 003, ...
# for num in range(1,21):
#     print( "대기번호 : " + str(num).zfill(3) )

# #표준 입력
# answer = input("아무 값이나 입력하세요 : ") #항상 문자열 형태로 입력이 되는 것을 알 수 있다.
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")


############### 다양한 출력
# # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500)) # > : rjust, 10 : 공간 총 20자리

# #양수일 때는 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# # 왼쪽 정렬하고, 빈칸을 _로 채움
# print("{0:_<+10}".format(500))

# #세자리 마다 콤마 찍어주기
# print("{0:,}".format(100000000000))
# print("{0:+,}".format(100000000000))
# print("{0:^<+30}".format(100000000000)) #빈공간 ^, 정렬 <, 부호 +-, 자릿수 30

# #소수점 출력
# print("{0:f}".format(5/3)) #f: float 자료형
# print("{0:.2f}".format(5/3))


# ######### 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") # w: to write
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") #a : append
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# #줄바꿈을 안하고 싶다면 end = "" 추가
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() #모든 라인을 가지고 와서 list 형태로 저장을 함
# for line in lines:
#     print(line, end="")

# score_file.close()


############# Pickle
# 프로그램상에 사용하는 데이터를 파일로 저장하는 것
# 다른 사람들도 피클을 이용해서 그 데이터를 사용할 수 있다.
# import pickle
# profile_file = open("profile.pickle", "wb") #w : write b : binary(필수), encoding 불필요
# profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #file에 있는 정보를 파이썬 상의 변수 profile에 저장
# print(profile)
# profile_file.close()



######## with (pickle 없이 활용할 수 있게 해준다, 그리고 매번 close를 해줄 필요가 없어서 좋다)
# import pickle
# with open("Profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# 단 네 줄로 파일을 쓰고 읽기
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

'''
Quiz) 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야한다.

- X 주차 주간보고 -
부서 : 
이름 : 
업무 요약 : 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작서하시오.

조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
'''

# for i in range(1, 51):
#     with open(str(i).zfill(2) +"주차.txt", "w", encoding="utf8") as Weekly_Report:
#         Weekly_Report.write("- {0} 주차 주간보고 -\n".format(i))
#         Weekly_Report.write("부서 : \n")
#         Weekly_Report.write("이름 : \n")
#         Weekly_Report.write("업무요약 : \n")
#         Weekly_Report.write("\n\n")



############ Class
# # 힘든 예
# # 마린 : 공격 유닛, 군인, 사격
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{0} 유닛이 생성 되었습니다.".format(name))
# print("체력 {0}, 공격력 {1} \n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크, 포 사격, 일반 모드/시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{0} 유닛이 생성 되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1} \n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35
# print("{0} 유닛이 생성 되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1} \n".format(tank2_hp, tank2_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# 클래스를 활용한 예
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, damage): # name, hp, damage는 멤버 변수, "."으로 접근할 수 있음
#         # __init__ : 객체 생성자 
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)

# #레이스 : 공중유닛, 비행기, 클로킹
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0}는 현재 크로킹 상태입니다.".format(wraith2.name))

# # 공격유닛
# class AttackUnit:
#     # class내에서의 method는 항상 self를 입력하고 간다
#     def __init__(self, name, hp, damage): # name, hp, damage는 멤버 변수, "."으로 접근할 수 있음
#         # __init__ : 객체 생성자 
#         self.name = name
#         self.hp = hp
#         self.damage = damage
    
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 파이어백 : 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어벳", 50, 16)
# firebat1.attack("5시")

# #공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


# ############ 상속
# # 일반 유닛 for 상속 exmaple
# class Unit:
#     def __init__(self, name, hp):
#         # __init__ : 객체 생성자 
#         self.name = name
#         self.hp = hp

# # 공격유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
    
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 파이어백 : 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어벳", 50, 16)
# firebat1.attack("5시")

# #공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


# ####### 다중 상속
# # 일반 유닛 for 상속 exmaple
# class Unit:
#     def __init__(self, name, hp, speed):
#         # __init__ : 객체 생성자 
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# # 공격유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
    
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# #드랍쉽 : 공중 유닛, 수송기
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# # 공중 공격유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed는 0으로 처리한 것
#         Flyable.__init__(self, flying_speed)
    
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 발키리 공격 유닛, 한번에 14발 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")



# ##### 연산자 오버로딩
# # 부모 클래스에서 정의한 매소드 말고 자식 클래스에서 정의한 매소드를 쓰고 싶을 때 매소드를 새로 정의해서 사용하는데 이를 오버로딩이라고 한다.

# #벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# #배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시") # 이 유닛이 지상 유닛인지 공중유닛인지 항상 파악해야해서 귀찮음! 그래서 오버로딩해서 fly말고 move만 써도 되게끔!
# '''
#     def move(self, location):
#     print("[공중 유닛 이동")
#     self.fly(self.name, location)
# ''' #이 부분을 추가하여 아래와 같이 만듦
# battlecruiser.move("9시")


# ########## pass
# # 건물
# class buildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass #일단은 완성된 걸로 치고 넘어가자! 라는 뜻

# # 서플라이 디폿 : 건물, 1개 건물 = 8, 유닛.
# supply_depot = buildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

# ############## super
# # 건물
# class buildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) #super를 통해서 초기화할때는 self정보를 넘겨주지 않아야함
#         self.location = location


# ############# class 상속 순서
# class Unit:
#     def __init__(self):
#         print("Unit 생성자")

# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")
# # 1)
# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         #super().__init__()
#         Unit.__init__(self)
#         Flyable.__init__(self)

# # # 2)
# # class FlyableUnit(Flyable, Unit):
# #     def __init__(self):
# #         super().__init__()

# # 1번과 2번의 순서에 따라 상속 결과가 다르다
# # 따라서 Super보다는 둘 다 각각의 부모 클래스를 거쳐 오는 것이 좋다

# #드랍쉽
# dropship = FlyableUnit()



# ##################### 스타크래프트 전반전 ###################### 프로젝트
# from random import randint

# # 일반 유닛 for 상속 exmaple
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 공격유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
    
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     #스팀팩
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -=10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족합니다.".format(self.name))
     
# #탱크
# class Tank(AttackUnit):
#     # 시즈모드 개발여부
#     seize_developed = False 

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         # 현재 시즈모드일 때 -> 시즈모드 해제
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

# #드랍쉽 : 공중 유닛, 수송기
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# # 공중 공격유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed는 0으로 처리한 것
#         Flyable.__init__(self, flying_speed)
    
#     def move(self, location):
#         self.fly(self.name, location)

# #레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False
#     def clocking(self):
#         if self.clocked == True:
#             print("{0} : 클로킹 모드 해제 합니다".format(self.name))
#             self.clocked = False
#         else:
#             print("{0} : 클로킹 모드 설정 합니다".format(self.name))
#             self.clocked = True

# ############################ 스타크래프트 후반전
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("GG")
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")

# # 실제 게임 시작
# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# # 레이스 1기 생성
# w1 = Wraith()

# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비 (탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):#지금 만들어진 객체가 어떤 클래스의 인스턴스인지 확인하는 것. # unit은 marine클래스의 인스턴스 인가?
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# #전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5,21)) # 공격은 랜덤으로 받음 (5~20)

# # 게임 종료
# game_over()




'''
Quiz 8) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]'''
# class House:
#     #매물 초기화
#     def __init__(self, location, House_type, deal_type, price, completion_year):
#         self.location = location
#         self.House_type = House_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self):
#         print("위치는 {0}, 주거 유형은 {1}, 거래 유형은 {2}, 가격은 {3}, 준공일은 {4}".format(self.location, self.House_type, self.deal_type, self.price, self.completion_year))

# houses = []
# B1 = House("강남", "아파트", "매매", "10억", "2010년")
# B2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# B3 = House("송파", "빌라", "월세", "500/50", "2000년")
# houses.append(B1)
# houses.append(B2)
# houses.append(B3)

# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     House.show_detail(house)

# #################### 예외 처리
# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1])) #실수했다고 가정하면!
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2] ))
# except ValueError:
#     print("에러! 잘못된 값을 입력하셨어요.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

#################### 에러 발생시키기
# # 사용자가 발생시키는 에러에 대해서 어떤 메세지를 찍을 지 정의할 수 있다.
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2) ) )
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally: ############### finally
#     # 프로그램 성사 여부에 관계 없이 무조건 출력됨
#     print("계산기를 이용해 주셔서 감사합니다.")


'''
Quiz9
동네에 항상 대기 손님이 있는 맛있는 치킨집이 있다.
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
    출력 메시지 : "잘못된 값을 입력하였습니다."
조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
    치킨소진시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
    출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

[코드]'''
# class SoldOutError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# chicken = 10;
# waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작
# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken: #남은 치킨보다 주문량이 많을때
#             print("재료가 부족합니다.\n")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.\n".format(waiting, order))
#             waiting += 1
#             chicken -= order

#         if chicken == 0:
#             raise SoldOutError("재고가 소진되어 더는 주문을 받지 않습니다.\n")

#     except ValueError:
#         print("잘 못된 값을 입력하셨습니다.\n")
    
#     except SoldOutError as err:
#         print(err)
#         break

    
# ################### 모듈 theater_module.py
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(1)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(1)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(3)
# price_soldier(3)


# from theater_module import price, price_morning
# price(3)
# price_morning(3)

# from theater_module import price_soldier as price
# price(5)


################ Package
# A set of modules
# 신규 여행사 프로젝트
# 태국, 베트남 
# import travel.thailand # import 뒤에는 모듈이나 패키지만 가능함
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # 여기서는 클래스 불러 올 수 있음
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# #################### __all__
# from travel import * # 모든 것들을 사용하겠다고 적었지만 import 하지 못함!
# trip_to = vietnam.VietnamPackage() #__init__.py로 가서 __all__ 조작 해주면 되는 것을 알 수 있음
# trip_to.detail()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()



# ##################### 모듈 직접 실행
# # 패키지와 모듈을 쓰기 전에 모듈과 패키지가 정상작동하는 지 확인할 필요가 있다.
# from travel import *
# # trip_to = vietnam.VietnamPackage()
# # trip_to.detail()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# # 모듈의 위치 확인
# import inspect
# import random
# print(inspect.getfile(random)) # directory 확인
# print(inspect.getfile(thailand)) # directory 확인

#################### pip install
# pypi.org
# beautifulsoup4
# pip install beautifulsoup4
# update : pip install --upgrade package's name
# delete : pip uninstall package's name

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


##################### 내장 함수
# # input : 사용자 입력을 받는 함수

# # dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# import random #외장함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

# or you can find many of those by searching on Google
"""list of python builtins"""



######################### 외장 함수
"""python module index on google"""
# # glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) #현재 디렉토리

# forlder = "sample_dir"

# if os.path.exists(forlder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(forlder)
#     print(forlder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(forlder) # 폴더생성
#     print(forlder, "폴더를 생성하였습니다.")

# import os
# print(os.listdir())

# # time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())

# # timedelta : 두 날짜사이의 간격
# today = datetime.date.today() #오늘 날짜 저장
# td = datetime.timedelta(days=100) 
# print("우리가 만난지 100일은 ", today + td)


'''
Quiz 10
프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

조건 : 모듈 파일명은 byme.py 로 작성

(모듈 사용 예제)
import  byme
byme.sign()

(출력 예제)
이 프로그램은 나도코딩에 의해 만들어 졌습니다.
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com
'''
# import byme
# byme.sign()