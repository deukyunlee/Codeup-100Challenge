# 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.

import sys

input = sys.stdin.readline().rstrip()

print(ord(input))