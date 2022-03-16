# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자. 

import sys

a, b = map(int,sys.stdin.readline().rstrip().split())

print(a-b)