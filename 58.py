# 2개의 정수값이 입력될 때, 
# 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자. 

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

if not bool(a) and not bool(b):
    print(True)

else:
    print(False)