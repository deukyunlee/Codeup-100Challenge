# 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자. 

import sys

f1, f2 = map(float,sys.stdin.readline().rstrip().split())

print(f1*f2)