# 두 정수(a, b)를 입력받아 
# a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

if a < b:
    print("True")
else:
    print("False")