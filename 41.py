# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자. 

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

print(a%b)