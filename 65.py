# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자. 

import sys

a,b,c = map(int, sys.stdin.readline().rstrip().split())

if a%2 == 0:
    print(a)

if b%2 == 0:
    print(b)

if c%2 == 0:
    print(c)