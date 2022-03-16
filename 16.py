# 공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자. 

import sys

a, b = map(str, sys.stdin.readline().rstrip().split())

print(b,a)