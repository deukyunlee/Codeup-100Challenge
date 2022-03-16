# 정수 2개를 입력받아 
# 합을 출력하는 프로그램을 작성해보자.

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

print(a+b)