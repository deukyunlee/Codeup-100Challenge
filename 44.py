# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자. 
# 단 0 <= a, b <= 2147483647, b는 0이 아니다. 

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print("{:.2f}".format(a/b))