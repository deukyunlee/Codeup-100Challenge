# 16진수를 입력받아 8진수(octal)로 출력해보자. 

import sys

input = int(sys.stdin.readline().rstrip(),16)

print("%o"%input)