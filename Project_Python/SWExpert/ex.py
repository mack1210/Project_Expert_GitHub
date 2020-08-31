T = int(input())
a = [0] * T
t = 0
for i in range(1, T+1):
    
    if T % i == 0:
        a[t] = i
        t += 1

if t == 2:
    for i in range(0, 2):
        print("{0}(은)는 {1}의 약수입니다.".format(a[i], T))
        
    print("{0}은 {1}과 {2}로만 나눌 수 있는 소수입니다.".format(T, a[0], a[1]))