# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자. 

# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D
# 로 평가되어야 한다.

import sys

n = int(sys.stdin.readline().rstrip())

if n>=90 and n<=100:
    print("A")

elif n>=70 and n<=89:
    print("B")

elif n>=40 and n<=69:
    print("C")

elif n>=0 and n<=39:
    print("D")