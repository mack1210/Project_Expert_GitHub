'''
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.


0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.


 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )

다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.


[입력 예]
3
5
49679
5
08271
10
7797946543

[출력 예]
#1 9 2
#2 8 1
#3 7 3
'''

# T = int()
# N = int()
# a = [[]]
# arr = []
# count = []
# count_Max = []
# a_index = []

# while T < 1 or T > 50:
#     T = int(input("T를 입력하세요 : "))

# for h in range(0, T):
#     a = [[0]]*T

# for i in range(1, T+1):

#     while N < 5 or N >100:
#         N = int(input("N을 입력하세요 : "))

#         while len(arr) != N:
#             arr = list(map(int, input()))
#             a[i-1] = arr
#             for j in set(arr):
#                 count.append(arr.count(j))
#             count_Max.append( max(count) )
#             a_index.append( count.index( max(count) ) )
#             count = []
#         arr = []
#     N = int()


# print("T : ", T)
# print("N : ", N)
# print("a : ", a)
# print("arr : ", arr)
# print("count : ", count)
# print("count_max : ", count_Max)
# print("a_index : ", a_index)
# for l in range(0, T):
#     print("set(a) : ", list(set(a[l]))[a_index[l]] )
# print()

# for k in range(0, T):
#     print("#{0} {1} {2}".format(k+1, list(set(a[k]))[a_index[k]], count_Max[k]))


T = int(input("T를 입력하세요 : "))
for i in range(1, T+1):
    N = int(input("N을 입력하세요 : "))
    a = input()
    a = [int(i) for i in a]
    print(a)
    for i in range(1, N)
        count = [0] * N

    for i in range(N):
        count[a[i]] += 1

    max_index, max_num = 0, 0
    for i in range(len(count)-1, -1, -1):
        if count[i] > max_index:
            max_index = count[i]
            max_num = i
    print("#{0} {1} {2}".format(T, max_num, max_index))
