# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자. 

import sys

input = int(sys.stdin.readline().rstrip())

print("%x"%input)