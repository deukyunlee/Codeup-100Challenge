# 6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자. 

import sys

s = sys.stdin.readline().rstrip()

print(s[0:2], s[2:4], s[4:6])