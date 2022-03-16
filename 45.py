# 정수 3개를 입력받아 합과 평균을 출력해보자.

import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())

print(a+b+c, "{:.2f}".format((a+b+c)/3))